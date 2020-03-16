-- final step from learndb.ru

SELECT e.employee_id,
       e.last_name,
       e.first_name,
       e.rank_id
  FROM employee e
 WHERE NOT EXISTS (SELECT 1
                     FROM employee m
                    WHERE m.manager_id = e.employee_id)
 ORDER BY e.last_name, e.employee_id
