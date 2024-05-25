from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from pymerc.api.models.common import InventoryAccountAsset, InventoryManager, Item
from pymerc.api.models.static import Recipe as RecipeModel

if TYPE_CHECKING:
    from pymerc.client import Client


class Recipe:
    def __init__(self, client: Client, recipe_name: str):
        self._client = client
        self.recipe_name = recipe_name
        self.data: Optional[RecipeModel] = None

    async def load(self):
        """Loads the data for the recipe and calculates labor required."""
        recipes = await self._client.static_api.get_recipes()
        for recipe in recipes:
            if recipe.name.value == self.recipe_name:
                self.data = recipe
        if self.data is None:
            raise ValueError(f"Recipe {self.recipe_name} not found")

    @property
    def labour(self) -> float:
        """Calculates the labor required for the recipe."""
        for input_ingredient in self.data.inputs:
            if input_ingredient.product == Item.Labour:
                return input_ingredient.amount
        return 0.0

    def calculate_target_labor(
        self,
        target: float,
        inventory_assets: Optional[dict[Item, InventoryAccountAsset]] = {},
        inventory_managers: Optional[dict[Item, InventoryManager]] = {},
    ) -> float:
        """Calculates the labor required for the given target multiplier.

        Args:
            target (float): The target percentage multiplier for the recipe.
            inventory_assets (Optional[List[InventoryAccountAsset]]): The list of inventory assets.
            inventory_managers (Optional[List[InventoryManager]]): The list of inventory managers.

        Returns:
            float: The labor required for the target multiplier.
        """
        for input_ingredient in self.data.inputs:
            if input_ingredient.product.name == "Labour":
                continue
            required_amount = input_ingredient.amount * target
            available_amount = 0

            asset = inventory_assets.get(input_ingredient.product)
            if asset:
                manager = (
                    inventory_managers.get(input_ingredient.product, None)
                    if inventory_managers
                    else None
                )
                buy_volume = manager.buy_volume if manager and manager.buy_volume else 0
                capacity = asset.capacity or asset.balance + buy_volume
                available_amount = min(
                    asset.balance - asset.reserved + buy_volume, capacity
                )

            if required_amount > available_amount:
                target = min(target, available_amount / input_ingredient.amount)

        labor_required = self.labour * target
        return labor_required
