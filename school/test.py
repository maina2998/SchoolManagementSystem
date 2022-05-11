from django.test import TestCase
from unittest import mock
from datetime import datetime




from school.models import (
    TeacherExtra,
    StudentExtra,
    
)


class  TeacherExtraTest(TestCase):
    def setUp(self):
            self.school=TeacherExtra(    
            status="Hello. My name is Love Lace. I love Akirachix",
            mobile="+254729113940",
           
            # salary=2021098877, 
            
            )
    def test_joindate(self):
        mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
    def test_status_contains_first_status(self):
            self.assertIn(self.school.status,self.school.status)
   
    
  
    

        





class StudentExtraTest(TestCase):
    def setUp(self):
            self.student=StudentExtra(
            status="Hello. My name is Love Lace. I love Akirachix",
            mobile="+254729113940",
            fee=2021098877, 
            
            )
    
    def setUp(self):
            self.school=StudentExtra(
            status="Hello. My name is Love Lace. I love Akirachix",
            mobile="+254729113940",
            )
      
       
    def test_mobile_contains_mobile(self):
            self.assertIn(self.school.mobile,self.school.mobile)
    def test_status_contains_first_status(self):
                self.assertIn(self.school.status,self.school.status)
    def test_cl_contains_cl(self):
                self.assertIn(self.school.cl,self.school.cl)

   
