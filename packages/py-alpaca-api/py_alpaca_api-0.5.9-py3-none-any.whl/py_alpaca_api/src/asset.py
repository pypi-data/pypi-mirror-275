import json
from typing import Dict

import pandas as pd
import requests

from .data_classes import AssetClass, asset_class_from_dict


class Asset:
    def __init__(self, trade_url: str, headers: Dict[str, str]) -> None:
        """Initialize Asset class

        Parameters:
        ___________
        trade_url: str
                Alpaca Trade API URL required

        headers: object
                API request headers required

        Raises:
        _______
        ValueError: If trade URL is not provided

        ValueError: If headers are not provided
        """  # noqa

        self.trade_url = trade_url
        self.headers = headers

    def get_all(
        self,
        status: str = "active",
        asset_class: str = "us_equity",
        exchange: str = "",
    ) -> pd.DataFrame:
        # Alpaca API URL for asset information
        url = f"{self.trade_url}/assets"

        params = {
            "status": status,
            "asset_class": asset_class,
            "exchange": exchange,
        }

        # Get request to Alpaca API for asset information
        response = requests.get(url, headers=self.headers, params=params)
        # Check if response is successful
        if response.status_code == 200:
            # Convert JSON response to dictionary
            res_df = pd.json_normalize(json.loads(response.text))

            res_df = res_df[res_df["status"] == "active"]
            res_df = res_df[res_df["fractionable"]]
            res_df = res_df[res_df["tradable"]]
            res_df = res_df[res_df["exchange"] != "OTC"]
            res_df.reset_index(drop=True, inplace=True)

            # Return asset information as an AssetClass object
            return res_df
        # If response is not successful, raise an exception
        else:
            raise ValueError(f"Failed to get asset information. Response: {response.text}")

    #####################################################
    # \\\\\\\\\\\\\\\\\\\  Get Asset ////////////////////#
    #####################################################
    def get(self, symbol: str) -> AssetClass:
        """
        Gets the asset information for a given symbol using the Alpaca API.

        Args:
            symbol (str): The symbol of the asset.

        Returns:
            AssetClass: The asset information as an AssetClass object.

        Raises:
            ValueError: If the request to the Alpaca API fails.

        Example:
            >>> asset = self.get("AAPL")
            >>> asset.symbol
            'AAPL'
            >>> asset.name
            'Apple Inc.'
            >>> asset.exchange
            'NASDAQ'
        """
        # Alpaca API URL for asset information
        url = f"{self.trade_url}/assets/{symbol}"
        # Get request to Alpaca API for asset information
        response = requests.get(url, headers=self.headers)
        # Check if response is successful
        if response.status_code == 200:
            # Convert JSON response to dictionary
            res = json.loads(response.text)
            # Return asset information as an AssetClass object
            return asset_class_from_dict(res)
        # If response is not successful, raise an exception
        else:
            raise ValueError(f"Failed to get asset information. Response: {response.text}")
