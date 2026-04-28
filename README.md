| Набір тестових даних  | Сортування включенням, час/пам’ять |  Сортування обміном, час/пам'ять  |  Сортування вибором, час/ пам’ять  |  Швидке сортування, час/ пам’ять  |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| n=100  | CPU Time: 0.03 sec(s)<br/>Memory: 9216 kilobyte(s) | CPU Time: 0.02 sec(s)<br/>Memory: 8960 kilobyte(s) | CPU Time: 0.02 sec(s)<br/>Memory: 8960 kilobyte(s) | CPU Time: 0.02 sec(s)<br/>Memory: 9088 kilobyte(s) |
| n=300  | CPU Time: 0.02 sec(s)<br/>Memory: 8960 kilobyte(s) | CPU Time: 0.03 sec(s)<br/>Memory: 8960 kilobyte(s) | CPU Time: 0.03 sec(s)<br/>Memory: 9216 kilobyte(s) | CPU Time: 0.03 sec(s)<br/>Memory: 9728 kilobyte(s) |
| n=500  | CPU Time: 0.02 sec(s)<br/>Memory: 9088 kilobyte(s) | CPU Time: 0.05 sec(s)<br/>Memory: 9216 kilobyte(s) | CPU Time: 0.03 sec(s)<br/>Memory: 9088 kilobyte(s) | CPU Time: 0.03 sec(s)<br/>Memory: 10240 kilobyte(s) |
| n=1000  | CPU Time: 0.02 sec(s)<br/>Memory: 9088 kilobyte(s) | CPU Time: 0.13 sec(s)<br/>Memory: 9088 kilobyte(s) | CPU Time: 0.05 sec(s)<br/>Memory: 9344 kilobyte(s) | CPU Time: 0.42 sec(s)<br/>Memory: 18176 kilobyte(s) |
| n=1500  |  JDoodle - output Limit reached. | JDoodle - output Limit reached. | JDoodle - output Limit reached. | JDoodle - output Limit reached. | JDoodle - output Limit reached. | CPU Time: 0.40 sec(s)<br/>Memory: 22400 kilobyte(s) |
| n=2000  |  JDoodle - output Limit reached. | JDoodle - output Limit reached. | JDoodle - output Limit reached. | JDoodle - output Limit reached. | JDoodle - output Limit reached. | CPU Time: 0.46 sec(s)<br/>Memory: 26496 kilobyte(s) |

***Загальний висновок: Для практичного застосування при невідомому або великому розмірі вхідних даних слід обирати Quick Sort. Прості методи (включення, вибір) краще використовувати лише для дуже малих масивів або в системах з обмеженою оперативною пам'яттю.***
