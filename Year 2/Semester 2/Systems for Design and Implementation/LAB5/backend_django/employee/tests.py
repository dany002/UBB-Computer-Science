import io
import json

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from employee.models import Project, Task, Team, Employee
from rest_framework.test import APITestCase


# Create your tests here.


class ProjectByAvgDifficultyiewTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(nameOfProject="Management System for LAB", clientName="Florin", budget=10000, description="This project develops software for the management system of the LAB.", status="active")
        Project.objects.create(nameOfProject="Payroll System", clientName="Marian", budget=20000, description="In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.", status="active")
        Project.objects.create(nameOfProject="Monitoring of Bandwidth", clientName="Deng Tsin Quin", budget=15000, description="This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.", status="on hold")
        Project.objects.create(nameOfProject="CRM – Customer Relationship Management", clientName="John", budget=7000, description="This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.", status="on hold")

        Team.objects.create(nameOfTeam="ClujCapitala", freePlaces=10, purpose="Development Team", admin="Daniel", rating=10)
        Team.objects.create(nameOfTeam="Aces", freePlaces=5, purpose="DevOps", admin="Florin", rating=7)
        Team.objects.create(nameOfTeam="The Ruin", freePlaces=7, purpose="Support", admin="Spencer", rating=9)
        Team.objects.create(nameOfTeam="Soul Crushers", freePlaces=3, purpose="QA", admin="Janos", rating=3)
        Team.objects.create(nameOfTeam="Gobstoppers", freePlaces=7, purpose="Security", admin="Karen", rating=4)

        Task.objects.create(nameOfTask="Alert the users of the due tasks.", difficulty=7, team_id=1, project_id=1)
        Task.objects.create(nameOfTask="They are user-friendly and therefore have higher adaptability.", difficulty=4, team_id=3, project_id=1)
        Task.objects.create(nameOfTask="Less time-consuming, and the users can easily navigate through.", difficulty=5, team_id=1, project_id=1)
        Task.objects.create(nameOfTask="It helps the brands to identify the products that have higher acceptance and materialise the resources for the same..", difficulty=10, team_id=3, project_id=3)
        Task.objects.create(nameOfTask="The images are encrypted; only the user having access can view them.", difficulty=8, team_id=1, project_id=2)

    def test_ProjectsByAvgDifficultyView(self):

        response = self.client.get("/projects/by-avg-difficulty")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

        dict_without_created = response.data
        for i in range(len(response.data)):
            dict_without_created[i].pop('created')

        result = JSONRenderer().render(dict_without_created) # transform to JSON from ordered dict.
        output_stream = io.BytesIO(result)
        data = JSONParser().parse(output_stream)

        expected_output = [
            {'id': 3,
             'nameOfProject': 'Monitoring of Bandwidth',
             'clientName': 'Deng Tsin Quin',
             'budget': 15000,
             'description': 'This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.',
             'status': 'on hold',
             'avg_difficulty': 10.0
             },
            {
                'id': 2,
                'nameOfProject': 'Payroll System',
                'clientName': 'Marian',
                'budget': 20000,
                'description': 'In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.',
                'status': 'active',
                'avg_difficulty': 8.0
            },
            {
                'id': 1,
                'nameOfProject': 'Management System for LAB',
                'clientName': 'Florin',
                'budget': 10000,
                'description': 'This project develops software for the management system of the LAB.',
                'status': 'active',
                'avg_difficulty': 5.333333333333333
            },
            {
                'id': 4,
                'nameOfProject': 'CRM – Customer Relationship Management',
                'clientName': 'John',
                'budget': 7000,
                'description': 'This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.',
                'status': 'on hold',
                'avg_difficulty': 0
            }
        ]
        self.assertEqual(expected_output, data)


class EmployeesByAvgDifficultyTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Project.objects.create(nameOfProject="Management System for LAB", clientName="Florin", budget=10000, description="This project develops software for the management system of the LAB.", status="active")
        Project.objects.create(nameOfProject="Payroll System", clientName="Marian", budget=20000, description="In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.", status="active")
        Project.objects.create(nameOfProject="Monitoring of Bandwidth", clientName="Deng Tsin Quin", budget=15000, description="This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.", status="on hold")
        Project.objects.create(nameOfProject="CRM – Customer Relationship Management", clientName="John", budget=7000, description="This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.", status="on hold")

        Team.objects.create(nameOfTeam="ClujCapitala", freePlaces=10, purpose="Development Team", admin="Daniel", rating=10)
        Team.objects.create(nameOfTeam="Aces", freePlaces=5, purpose="DevOps", admin="Florin", rating=7)
        Team.objects.create(nameOfTeam="The Ruin", freePlaces=7, purpose="Support", admin="Spencer", rating=9)
        Team.objects.create(nameOfTeam="Soul Crushers", freePlaces=3, purpose="QA", admin="Janos", rating=3)
        Team.objects.create(nameOfTeam="Gobstoppers", freePlaces=7, purpose="Security", admin="Karen", rating=4)

        Task.objects.create(nameOfTask="Alert the users of the due tasks.", difficulty=7, team_id=1, project_id=1)
        Task.objects.create(nameOfTask="They are user-friendly and therefore have higher adaptability.", difficulty=4, team_id=3, project_id=1)
        Task.objects.create(nameOfTask="Less time-consuming, and the users can easily navigate through.", difficulty=5, team_id=1, project_id=1)
        Task.objects.create(nameOfTask="It helps the brands to identify the products that have higher acceptance and materialise the resources for the same..", difficulty=10, team_id=3, project_id=3)
        Task.objects.create(nameOfTask="The images are encrypted; only the user having access can view them.", difficulty=8, team_id=1, project_id=2)

        Employee.objects.create(firstName="Daniel", lastName="Moldovan", employmentDate="2015-02-15",phoneNumber="07122532412",email="daniel@gmail.com", wage=9000, team_id=1)
        Employee.objects.create(firstName="George", lastName="Rapeanu", employmentDate="2020-11-20",phoneNumber="07235214912",email="george@gmail.com", wage=9010, team_id=1)
        Employee.objects.create(firstName="Alin", lastName="Pop", employmentDate="2021-02-02",phoneNumber="0746345981",email="alin@gmail.com", wage=5000, team_id=3)
        Employee.objects.create(firstName="Bogdan", lastName="Teodorescu", employmentDate="2022-05-10",phoneNumber="07534512592",email="bogdan@gmail.com", wage=7500, team_id=2)
        Employee.objects.create(firstName="Karen", lastName="Brown", employmentDate="2010-04-18",phoneNumber="0753253406",email="karen@gmail.com", wage=1000, team_id=3)


    def test_EmployeesByAvgDifficultyView(self):
        response = self.client.get("/employees/by-avg-difficulty")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)

        result = JSONRenderer().render(response.data)  # transform to JSON from ordered dict.
        output_stream = io.BytesIO(result)
        data = JSONParser().parse(output_stream)

        expected_output = [
            {
                'id': 3,
                'firstName': 'Alin',
                'lastName': 'Pop',
                'employmentDate': '2021-02-02',
                'phoneNumber': '0746345981',
                'email': 'alin@gmail.com',
                'wage': 5000,
                'avg_difficulty': 7.0
            },
            {
                'id': 5,
                'firstName': 'Karen',
                'lastName': 'Brown',
                'employmentDate': '2010-04-18',
                'phoneNumber': '0753253406',
                'email': 'karen@gmail.com',
                'wage': 1000,
                'avg_difficulty': 7.0
            },
            {
                'id': 1,
                'firstName': 'Daniel',
                'lastName': 'Moldovan',
                'employmentDate': '2015-02-15',
                'phoneNumber': '07122532412',
                'email': 'daniel@gmail.com',
                'wage': 9000,
                'avg_difficulty': 6.666666666666667
            },
            {
                'id': 2,
                'firstName': 'George',
                'lastName': 'Rapeanu',
                'employmentDate': '2020-11-20',
                'phoneNumber': '07235214912',
                'email': 'george@gmail.com',
                'wage': 9010,
                'avg_difficulty': 6.666666666666667
            },
            {
                'id': 4,
                'firstName': 'Bogdan',
                'lastName': 'Teodorescu',
                'employmentDate': '2022-05-10',
                'phoneNumber': '07534512592',
                'email': 'bogdan@gmail.com',
                'wage': 7500,
                'avg_difficulty': 0
            }
        ]

        self.assertEqual(expected_output, data)



# class ProjectListViewTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         #nameOfProject = models.CharField(max_length=200)
#         #clientName = models.CharField(max_length=200)
#         #budget = models.IntegerField()
#         #description = models.CharField(max_length=200)
#         #status = models.CharField(max_length=200)
#         Project.objects.create(nameOfProject="Management System for LAB", clientName="Florin", budget=10000, description="This project develops software for the management system of the LAB.", status="active")
#         Project.objects.create(nameOfProject="Payroll System", clientName="Marian", budget=20000, description="In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.", status="active")
#         Project.objects.create(nameOfProject="Monitoring of Bandwidth", clientName="Deng Tsin Quin", budget=15000, description="This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.", status="on hold")
#         Project.objects.create(nameOfProject="CRM – Customer Relationship Management", clientName="John", budget=7000, description="This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.", status="on hold")
#
#         Team.objects.create(nameOfTeam="ClujCapitala", freePlaces=10, purpose="Development Team", admin="Daniel", rating=10)
#         Team.objects.create(nameOfTeam="Aces", freePlaces=5, purpose="DevOps", admin="Florin", rating=7)
#         Team.objects.create(nameOfTeam="The Ruin", freePlaces=7, purpose="Support", admin="Spencer", rating=9)
#         Team.objects.create(nameOfTeam="Soul Crushers", freePlaces=3, purpose="QA", admin="Janos", rating=3)
#         Team.objects.create(nameOfTeam="Gobstoppers", freePlaces=7, purpose="Security", admin="Karen", rating=4)
#
#         Task.objects.create(nameOfTask="Alert the users of the due tasks.", difficulty=7, team=1, project=1)
#         Task.objects.create(nameOfTask="They are user-friendly and therefore have higher adaptability.", difficulty=4, team=3, project=1)
#         Task.objects.create(nameOfTask="Less time-consuming, and the users can easily navigate through.", difficulty=5, team=1, project=1)
#         Task.objects.create(nameOfTask="It helps the brands to identify the products that have higher acceptance and materialise the resources for the same..", difficulty=10, team=5, project=5)
#         Task.objects.create(nameOfTask="The images are encrypted; only the user having access can view them.", difficulty=8, team=1, project=1)
#
#     @mock.patch('requests.get')
#     def test_url_exist(self, mock_get):
#         team = 1
#         response_data = MagicMock()
#         #mock_get.json.return_value = {'id': '1'}
#         #data = json.loads(mock_get.json.return_value)
#         response = requests.get('/projects/')
#         print(response.content)
#         #response = self.client.get("/projects/")
#         #self.assertEqual(response.status_code, 200)
#         #print(response.data)
#
# class ProjectListViewTestCase(APITestCase):
#
#     @mock.patch('requests.get')
#     def test_get_data_success(self, mock_get):
#         mock_response = mock.Mock(status_code=status.HTTP_200_OK)
#         mock_response.json.return_value = {'data' : 'Hello World'}
#
#         mock_get.return_value = mock_response
#
#         response = self.client.get('/projects/')
#         print(response.status_code)
#         print(response.content)
#         #print(response.json)

# class ProjectListViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#
#         Project.objects.create(nameOfProject="Management System for LAB", clientName="Florin", budget=10000, description="This project develops software for the management system of the LAB.", status="active")
#         Project.objects.create(nameOfProject="Payroll System", clientName="Marian", budget=20000, description="In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.", status="active")
#         Project.objects.create(nameOfProject="Monitoring of Bandwidth", clientName="Deng Tsin Quin", budget=15000, description="This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.", status="on hold")
#         Project.objects.create(nameOfProject="CRM – Customer Relationship Management", clientName="John", budget=7000, description="This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.", status="on hold")
#
#         Team.objects.create(nameOfTeam="ClujCapitala", freePlaces=10, purpose="Development Team", admin="Daniel", rating=10)
#         Team.objects.create(nameOfTeam="Aces", freePlaces=5, purpose="DevOps", admin="Florin", rating=7)
#         Team.objects.create(nameOfTeam="The Ruin", freePlaces=7, purpose="Support", admin="Spencer", rating=9)
#         Team.objects.create(nameOfTeam="Soul Crushers", freePlaces=3, purpose="QA", admin="Janos", rating=3)
#         Team.objects.create(nameOfTeam="Gobstoppers", freePlaces=7, purpose="Security", admin="Karen", rating=4)
#
#         Task.objects.create(nameOfTask="Alert the users of the due tasks.", difficulty=7, team=1, project=1)
#         Task.objects.create(nameOfTask="They are user-friendly and therefore have higher adaptability.", difficulty=4, team=3, project=1)
#         Task.objects.create(nameOfTask="Less time-consuming, and the users can easily navigate through.", difficulty=5, team=1, project=1)
#         Task.objects.create(nameOfTask="It helps the brands to identify the products that have higher acceptance and materialise the resources for the same..", difficulty=10, team=5, project=5)
#         Task.objects.create(nameOfTask="The images are encrypted; only the user having access can view them.", difficulty=8, team=1, project=1)
#
#
#     @patch('employee.views.ProjectList.get')
#     def test_non_crud_view(self, mock_get):
#         mock_data = {'key': 'value'}
#         mock_response = Mock(status_code=200, json=mock_data)
#         mock_get.return_value = mock_response
#
#         # Make a request to the non-CRUD view
#         url = reverse('/projects/')
#         #response = self.client.get(url)
#         self.assertEqual(1,1)
#         # Check that the response is correct
#         #self.assertEqual(response.status_code, 200)
#         #self.assertEqual(response.json(), mock_data)
#
#
# # class GetWeatherTestCase(TestCase):
# #     @patch('myapp.views.requests.get')
# #     def test_get_weather(self, mock_get):
# #         city = 'london'
# #         response_data = {'weather': [{'description': 'clear sky'}]}
# #         mock_get.return_value.json.return_value = response_data
# #         response = self.client.get('/get-weather/', {'city': city})
# #         self.assertEqual(response.status_code, 200)
# #         self.assertEqual(json.loads(response.content), response_data)
#





