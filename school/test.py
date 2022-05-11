from django.test import TestCase
from unittest import mock
from datetime import datetime


from school.models import (
    TeacherExtra,
    StudentExtra,
    
)


class  TeacherExtraTest(TestCase):
    def test_default_values(self):
        mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
            mock_now.return_value = mock_date
        self.assertEquals(TeacherExtra.salary, False)
        self.assertEquals(TeacherExtra.mobile, 40)
        self.assertEquals(TeacherExtra.status, False)
        # self.assertEquals(user.created_at, mock_date)
        # self.assertEquals(user.updated_at, mock_date)
    # def TeacherExtra(self):
    #     site_config = TeacherExtra.objects.create(key="akey", value="aname")
    #     self=user.OneToOneField(User,on_delete=models.CASCADE)
    #     salary = models.PositiveIntegerField(null=False)
    #     joindate=models.DateField(auto_now_add=True)
    #     mobile = models.CharField(max_length=40)
    #     status=models.BooleanField(default=False) 
    # def TeacherExtra(self):
    #     mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
    #     with mock.patch('django.utils.timezone.now') as mock_now:
    #         mock_now.return_value = mock_date
    #     self.assertEquals(self.mobile, 40)
    #     self.assertEquals(self.salary, True)
    #     self.assertEquals(self.status, False)
    #     self.assertEquals(self.created_at, mock_date)





class StudentExtraTest(TestCase):
     def test_default_values(self):
        mock_date = datetime(2021, 3, 4, 14, 57, 11, 703055)
        with mock.patch('django.utils.timezone.now') as mock_now:
                mock_now.return_value = mock_date
        self.assertEquals(StudentExtra.roll, False)
        self.assertEquals(StudentExtra.mobile, True)
        self.assertEquals(StudentExtra.status, False)
        self.assertEquals(StudentExtra.cl, 1)

    # def StudentExtra(self):
    #     self.assertEquals(self.roll, 10)
    #     self.assertEquals(self.salary, True)
    #     self.assertEquals(self.status, False)
    #     self.assertEquals(self.mobile,10,1)
    #     self.assertEquals(self.cl, True)
    #     self.assertEquals(self.status, False)
    #     term =StudentExtra.objects.create(name="test Term", current=True)
    #     self.assertEqual(str(term), "test Term")
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    # roll = models.CharField(max_length=10)
    # mobile = models.CharField(max_length=40,null=True)
    # fee=models.PositiveIntegerField(null=True)
    # cl= models.CharField(max_length=10,choices=classes,default='one')
    # status=models.BooleanField(default=False)

      

