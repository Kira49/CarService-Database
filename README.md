# Team DataOrData

## Instructions to run

```console
$ mysql -h 127.0.0.1 -u root --port=5005 -p < dump.sql
```
Enter your password on prompt, and then run
```console
$ python3 new.py
```
The terminal should now look like this
```console
connected
Press any key to continue>
```
Press any key, and now the terminal should look like this
```console
1. Add Customer
2. Add Spare
3. Add Employee
4. Add Warehouse
5. Add Garage
6. Add Cars
7. Add Service History
8. Delete Car
9. Delete Employee
10. Delete Spare
11. Selection Query
12. Search Spare parts
13. Search Car
14. Update Service history
15. Update Customer details
16. Update Employee details
17. Update Spare part details
18. Update service status
19. Projection Query
0. Quit
Enter choice>
```
Enter a number depending on what you want to query, like

```console
Enter choice> 2
```
Terminal will now prompt your input depending on your query

```console
Enter details:
Type ID:
```
