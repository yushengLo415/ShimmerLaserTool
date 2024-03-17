# ShimmerLaserTool
ShimmerLaserTool is an application designed for calculating laser cutting costs and generating sales receipts.

## User Interface
![image](https://github.com/yushengLo415/ShimmerLaserTool/blob/master/img/UI.jpg)

## Overview of Features
- Cost Calculation: Calculate the cost of laser cutting based on different metal materials and thicknesses.
- Sales Receipt Generation: Provide a simple interface for users to input product details and generate sales receipts.

## Usage Instructions
1. Configure Database Settings: Before launching the application, configure the database settings in db_setting.json.
2. Input Metal Prices: Input the unit prices for different metals within the application.
3. Add Product Information: Use the plus or minus buttons to add or remove products, then fill in the details for each product.
4. Calculate Costs: Click the calculate button to compute the laser cutting cost for each product.
5. Generate Receipts: Fill in the relevant information for the receipt, then click the screenshot button to save the generated sales receipt image.
6. Automatic Saving: When the application is closed, all data will be automatically saved to the database without manual intervention.

## Additional Information
|Thickness| steel | stainless steel | aluminum | hole |
| :-: | :-: | :-: | :-: | :-: |
| 0 | 0 | 0 | 0 | 0 |
| 1 | 20 | 40 | 40 | 2 |
| 2 | 20 | 40 | 40 | 2 |
| 3 | 30 | 60 | 60 | 2 |
| 4 | 40 | 80 | 80 | 2 |
| 5 | 50 | 100 | 100 | 3 |
| 6 | 60 | 120 | 120 | 3 |
| 8 | 80 | 160 | 160 | 4 |
| 9 | 90 | 180 | 180 | 4 |
| 10 | 100 | 200 | 200 | 4 |
| 12 | 120 | 240 | 240 | 4 |
| 16 | 200 | 400 | 400 | 6 |
| 20 | 300 | 600 | 600 | 8 |

Thickness vs. Price Chart: Provides laser cutting prices for different thicknesses per meter, along with price adjustments for hole sizes.
