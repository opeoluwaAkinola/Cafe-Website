import csv
with open('cafe-data.csv', newline='',encoding="utf8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    print(csv_data)
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)
print(list_of_rows)
# <!--	  <table class="table">-->
# <!--          <thead>-->
# <!--          <tr>-->
# <!--              {% for stuff in cafes[0] %}-->
# <!--            <th scope="col">{{stuff}</th>-->
# <!--            {% endfor %}-->
# <!--            </tr>-->
# <!--          </thead>-->
# <!--          <tbody>-->
# <!--          {% for cafe in cafes[1:] %}-->
# <!--            <tr>-->
# <!--              {% for stuff in cafe %}-->
# <!--            <td scope="col">{{stuff}</td>-->
# <!--            {% endfor %}-->
# <!--            </tr>-->
# <!--            {% endfor %}-->
# <!--          </tbody>-->
# <!--  	  </table>-->
# <!--      <p>{{cafes}}</p>-->