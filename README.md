# Tivix Code Test
This is the code test for Tivix. 
Two models -> Teacher and Student, teacher can have multiple students and student can have multiple teachers. Also, the teacher can mark her student as favourite or not. 

# Installation
This django app has been dockerized.
1. Clone it<br>
2. Run the command 'docker-compose up'

If you want to run without Docker. Simply clone and run
```
pip install -r requirements.txt
python manage.py runserver
```

The app comes with a database with test data. So, no need to makemigrations and migrate.

# GraphQL Queries
GraphQL browser can be accessed at localhost:8000/graphql or 0.0.0.0:8000/graphql or 127.0.0.1:8000/graphql

Sample Queries for GraphQL<br>
**Fetching all teachers**
```
allTeachers{
  edges{
    node{
      name, subject, id
    }
  }
}
```
**To get all students in a teacher**
```
query{
  allTeachers{
    edges{
      node{
        name, subject, id
        students: student{
          id, name, age
        }
      }
    }
  }
}
```
**To get all students that have been marked as favorite by the teacher**
```
query{
  allTeachers{
    edges{
      node{
        name, subject
        teacher(favorite:"TRUE"){
          edges{
            node{
              student{
                id,name
              }
            }
          }
        }
      }
    }
  }
}
```

# Tests
Tests can be run by running the command python manage.py tests. Note: The last test is supposed to fail. If it fails, it means it works. Because, the statement that should be returning True is being evaluated using self.assertFalse()

# Admin User
SuperUser credentials if you wish to  access the admin panel:<br>
Username: dhruvarora<br>
Password: dillirox123<br>

Or you can always run **python manage.py createsuperuser** to create a new super user