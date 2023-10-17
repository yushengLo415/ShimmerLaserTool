# ShimmerLaserTool
Calculating laser cutting cost and generating a sales slip

## User Interface
![image](https://github.com/yushengLo415/ShimmerLaserTool/blob/master/img/UI.jpg)

## How to use
1. Configure db_setting in db_setting.json before launching
2. Input the price of different metal
3. Click/Minus plus button to add new products/delete products
4. Input the product details, including product name, count, metal type, area($mm^2$), thickness, length of laser cutting line($m$), count of holes
5. Click compute button(the calculator one), it will compute all information of the product
6. Fill up information such as address, phone number, date, client, order id
7. Click screenshot button and save the picture
8. When the application is closed, all data will be automatically saved into database

## Additional
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

Laser cutting price in different thickness (per meter).  
If radius of holes greater than 7mm, it would be double price.

## Environment
python 3.10.6  
QT5  
MySQL  
