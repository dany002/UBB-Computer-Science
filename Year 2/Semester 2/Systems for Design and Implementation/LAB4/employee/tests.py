from django.test import TestCase, RequestFactory
from unittest.mock import patch
from django.urls import reverse
from employee.views import ProjectsByAvgDifficulty

# Create your tests here.

class ProjectsByAvgDifficultyViewTestCase(TestCase):
    # def setUp(self):
    #     self.factory = RequestFactory()

    @patch('employee.views.ProjectsByAvgDifficulty')
    def test_view(self, mock_service):
        mock_instance = mock_service.return_value
        mock_instance.get_data.return_value = [{
        "id": 7,
        "created": "2023-03-21T13:29:24.883887Z",
        "nameOfProject": "Sentiment analysis for product rating",
        "clientName": "George",
        "budget": 30000,
        "description": "This project aims to develop a sentiment analysis system for product rating. It is an e-commerce web application.",
        "status": "active",
        "avg_difficulty": 10.0
        },
        {
        "id": 6,
        "created": "2023-03-21T13:28:48.335263Z",
        "nameOfProject": "Android task monitoring",
        "clientName": "Daniel",
        "budget": 20000,
        "description": "The project is primarily a reminder app powered by an AI chatbot that reminds users of all the tasks that are due daily.",
        "status": "on hold",
        "avg_difficulty": 9.0
        },
        {
        "id": 9,
        "created": "2023-03-21T13:32:48.272677Z",
        "nameOfProject": "Image encryption using AES algorithm",
        "clientName": "Chong Chiun",
        "budget": 50000,
        "description": "This project seeks to create a sophisticated image encryption system by using the AES algorithm to prevent intrusion attacks of imaging systems and misuse of digital images.",
        "status": "on hold",
        "avg_difficulty": 6.5
        },
        {
        "id": 10,
        "created": "2023-03-21T13:34:00.792747Z",
        "nameOfProject": "Weather forecasting system",
        "clientName": "Henry Steve",
        "budget": 14200,
        "description": "Weather forecasting systems use a combination of science and technology to make accurate predictions on weather conditions of a particular location at a particular time.",
        "status": "active",
        "avg_difficulty": 6.0
        },
        {
        "id": 1,
        "created": "2023-03-21T13:22:39.419200Z",
        "nameOfProject": "Management System for LAB",
        "clientName": "Florin",
        "budget": 10000,
        "description": "This project develops software for the management system of the LAB.",
        "status": "active",
        "avg_difficulty": 5.75
        },
        {
        "id": 4,
        "created": "2023-03-21T13:27:03.787605Z",
        "nameOfProject": "CRM – Customer Relationship Management",
        "clientName": "John",
        "budget": 7000,
        "description": "This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.",
        "status": "on hold",
        "avg_difficulty": 5.0
        },
        {
        "id": 2,
        "created": "2023-03-21T13:24:33.858578Z",
        "nameOfProject": "Payroll System",
        "clientName": "Marian",
        "budget": 20000,
        "description": "In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.",
        "status": "active",
        "avg_difficulty": 0
        },
        {
        "id": 3,
        "created": "2023-03-21T13:26:19.576481Z",
        "nameOfProject": "Monitoring of Bandwidth",
        "clientName": "Deng Tsin Qin",
        "budget": 15000,
        "description": "This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.",
        "status": "on hold",
        "avg_difficulty": 0
        },
        {
        "id": 5,
        "created": "2023-03-21T13:27:40.017302Z",
        "nameOfProject": "Tracking System for Defects",
        "clientName": "Karen",
        "budget": 1500,
        "description": "This is a bug tracking and error system based on the web. This project is very helpful for mini teams who are working on manufacturing and software projects.",
        "status": "on hold",
        "avg_difficulty": 0
        },
        {
        "id": 8,
        "created": "2023-03-21T13:31:28.249178Z",
        "nameOfProject": "Fingerprint-based ATM system",
        "clientName": "Eduard Hellvig",
        "budget": 100000,
        "description": "Users need not carry their ATM cards with them at all times – they can use their fingerprints to access ATM services.",
        "status": "active",
        "avg_difficulty": 0
        }]
        #request = self.factory.get(reverse('projects-by-avg-difficulty'),{'created' : 1})
        #response = ProjectsByAvgDifficulty.as_view()(request)

        expected_data = [{"id": 7,
        "created": "2023-03-21T13:29:24.883887Z",
        "nameOfProject": "Sentiment analysis for product rating",
        "clientName": "George",
        "budget": 30000,
        "description": "This project aims to develop a sentiment analysis system for product rating. It is an e-commerce web application.",
        "status": "active",
        "avg_difficulty": 10.0
        },
        {
        "id": 6,
        "created": "2023-03-21T13:28:48.335263Z",
        "nameOfProject": "Android task monitoring",
        "clientName": "Daniel",
        "budget": 20000,
        "description": "The project is primarily a reminder app powered by an AI chatbot that reminds users of all the tasks that are due daily.",
        "status": "on hold",
        "avg_difficulty": 9.0
        },
        {
        "id": 9,
        "created": "2023-03-21T13:32:48.272677Z",
        "nameOfProject": "Image encryption using AES algorithm",
        "clientName": "Chong Chiun",
        "budget": 50000,
        "description": "This project seeks to create a sophisticated image encryption system by using the AES algorithm to prevent intrusion attacks of imaging systems and misuse of digital images.",
        "status": "on hold",
        "avg_difficulty": 6.5
        },
        {
        "id": 10,
        "created": "2023-03-21T13:34:00.792747Z",
        "nameOfProject": "Weather forecasting system",
        "clientName": "Henry Steve",
        "budget": 14200,
        "description": "Weather forecasting systems use a combination of science and technology to make accurate predictions on weather conditions of a particular location at a particular time.",
        "status": "active",
        "avg_difficulty": 6.0
        },
        {
        "id": 1,
        "created": "2023-03-21T13:22:39.419200Z",
        "nameOfProject": "Management System for LAB",
        "clientName": "Florin",
        "budget": 10000,
        "description": "This project develops software for the management system of the LAB.",
        "status": "active",
        "avg_difficulty": 5.75
        },
        {
        "id": 4,
        "created": "2023-03-21T13:27:03.787605Z",
        "nameOfProject": "CRM – Customer Relationship Management",
        "clientName": "John",
        "budget": 7000,
        "description": "This CRM project is an integrated approach of E-mail and user management to acquiring, recognizing & maintaining customers.",
        "status": "on hold",
        "avg_difficulty": 5.0
        },
        {
        "id": 2,
        "created": "2023-03-21T13:24:33.858578Z",
        "nameOfProject": "Payroll System",
        "clientName": "Marian",
        "budget": 20000,
        "description": "In an organization, payroll details maintenance, as well as the pay, slips preparation every month is a time-consuming, laborious, and time-consuming process.",
        "status": "active",
        "avg_difficulty": 0
        },
        {
        "id": 3,
        "created": "2023-03-21T13:26:19.576481Z",
        "nameOfProject": "Monitoring of Bandwidth",
        "clientName": "Deng Tsin Qin",
        "budget": 15000,
        "description": "This project implements a system to monitor the bandwidth (BW) who wishes to check their BW for their internet plan.",
        "status": "on hold",
        "avg_difficulty": 0
        },
        {
        "id": 5,
        "created": "2023-03-21T13:27:40.017302Z",
        "nameOfProject": "Tracking System for Defects",
        "clientName": "Karen",
        "budget": 1500,
        "description": "This is a bug tracking and error system based on the web. This project is very helpful for mini teams who are working on manufacturing and software projects.",
        "status": "on hold",
        "avg_difficulty": 0
        },
        {
        "id": 8,
        "created": "2023-03-21T13:31:28.249178Z",
        "nameOfProject": "Fingerprint-based ATM system",
        "clientName": "Eduard Hellvig",
        "budget": 100000,
        "description": "Users need not carry their ATM cards with them at all times – they can use their fingerprints to access ATM services.",
        "status": "active",
        "avg_difficulty": 0
        }]

        response = self.client.get('employees/by-avg-difficulty')
        print(response.content)
        #response.render()
        #print(response.content)
        #self.assertJSONEqual(response.content, expected_data)
