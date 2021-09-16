{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyPNRCX28QrJZZOXYNKToaeF",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/veekshith21/oop.py/blob/main/lab%20assingmnet%202.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "n5I56doaaHlO"
      },
      "source": [
        "problem 1"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EflgjzcnTi1k",
        "outputId": "12c08ebb-3fb5-4329-fbad-5615c0dc74f0"
      },
      "source": [
        "import math\n",
        "class Circle:\n",
        "    def __init__(self, radius):\n",
        "        self.radius = radius\n",
        "\n",
        "    def perimeter(self):\n",
        "        return (2 * math.pi * self.radius)\n",
        "\n",
        "    def area(self):\n",
        "        return (math.pi * (self.radius ** 2))\n",
        "\n",
        "c1 = Circle(4)\n",
        "print(c1.perimeter())\n",
        "print(c1.area())"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "25.132741228718345\n",
            "50.26548245743669\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "KNmQKs7CaNxy"
      },
      "source": [
        "2"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "skzRR6vZT3oo",
        "outputId": "660a39f7-66b9-4662-d55d-057ef0f38366"
      },
      "source": [
        "class TeachingFaculty:\n",
        "    # def _init_(self, name, emp_ID, branch, salary):\n",
        "    \n",
        "\n",
        "    def setData(self):\n",
        "        self.name = input(\"Enter the employee name : \")       #     self.name = name\n",
        "        self.emp_ID = int(input(\"Enter the employee ID : \"))  #     self.emp_ID = emp_ID\n",
        "        self.branch = input(\"Enter the branch name : \")       #     self.branch = branch\n",
        "        self.salary = int(input(\"Enter the salary : \"))       #     self.salary = salary\n",
        "\n",
        "    def getData(self):\n",
        "        print(f\"Name : {self.name} \\nEmployee ID : {self.emp_ID} \\nBranch : {self.branch} \\nSalary : {self.salary}\\n\")\n",
        "        return self.name, self.emp_ID, self.branch, self.salary\n",
        "\n",
        "# t1 = TeachingFaculty()\n",
        "listTF = []\n",
        "for i in range(1, 3):\n",
        "    temp = TeachingFaculty()\n",
        "    print(f\"\\nEnter the data for {i}th employee : \")\n",
        "    temp.setData()\n",
        "    listTF.append(temp)\n",
        "\n",
        "for i in range(0, 2):\n",
        "    print(f\"\\nData of {i+1}th employee : \")\n",
        "    listTF[i].getData()"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Enter the data for 1th employee : \n",
            "Enter the employee name : veekshith\n",
            "Enter the employee ID : 45\n",
            "Enter the branch name : cse\n",
            "Enter the salary : 200000\n",
            "\n",
            "Enter the data for 2th employee : \n",
            "Enter the employee name : arjun\n",
            "Enter the employee ID : 98\n",
            "Enter the branch name : cse\n",
            "Enter the salary : 3000000\n",
            "\n",
            "Data of 1th employee : \n",
            "Name : veekshith \n",
            "Employee ID : 45 \n",
            "Branch : cse \n",
            "Salary : 200000\n",
            "\n",
            "\n",
            "Data of 2th employee : \n",
            "Name : arjun \n",
            "Employee ID : 98 \n",
            "Branch : cse \n",
            "Salary : 3000000\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ECBgBGLWaPY-"
      },
      "source": [
        "3"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PAzjJ_8iUauN",
        "outputId": "f66690bb-516e-406a-cc3d-2921a7a681bd"
      },
      "source": [
        "class Account:\n",
        "    def __init__(self, accNo, accHolder, amount):\n",
        "        self.accountNumber = accNo\n",
        "        self.accountHolder = accHolder\n",
        "        self.accountAmount = amount\n",
        "\n",
        "    def deposit(self):\n",
        "        depAmount = int(input(\"Enter the amount to deposit : \"))\n",
        "        self.accountAmount += depAmount\n",
        "        print(f\"Amount deposited : {depAmount} \\nNew Balance : {self.accountAmount}\")\n",
        "\n",
        "    def withdraw(self):\n",
        "        withAmount = int(input(\"Enter the amount to withdraw : \"))\n",
        "        if withAmount > self.accountAmount:\n",
        "            print(\"Cannot withdraw more than savings.\")\n",
        "            return -1\n",
        "        self.accountAmount -= withAmount\n",
        "        print(f\"Amount withdraw : {withAmount} \\nNew Balance = {self.accountAmount}\")\n",
        "        return withAmount\n",
        "\n",
        "    def checkBalance(self):\n",
        "        print(f\"Balance : {self.accountAmount}\")\n",
        "        return self.accountAmount\n",
        "\n",
        "    def getDetails(self):\n",
        "        print(f\"\\nAccount Number : {self.accountNumber} \\nAccount Holder : {self.accountHolder} \\nBalance : {self.accountAmount}\")\n",
        "        return self.accountNumber, self.accountHolder, self.accountAmount\n",
        "\n",
        "a1 = Account(509456, \"VICKY R\", 500)\n",
        "a1.deposit()\n",
        "withdraw = a1.withdraw()\n",
        "# print(withdraw)\n",
        "balance = a1.checkBalance()\n",
        "# print(balance)\n",
        "details = a1.getDetails()\n",
        "# print(details)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the amount to deposit : 3800\n",
            "Amount deposited : 3800 \n",
            "New Balance : 4300\n",
            "Enter the amount to withdraw : 5000\n",
            "Cannot withdraw more than savings.\n",
            "Balance : 4300\n",
            "\n",
            "Account Number : 509456 \n",
            "Account Holder : VICKY R \n",
            "Balance : 4300\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Br9QLPsnaQUG"
      },
      "source": [
        "4"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SdOjyuErV2bY",
        "outputId": "7aa7aad6-708a-4f39-ddd0-457cc8127b34"
      },
      "source": [
        "class Records:\n",
        "\n",
        "    def setData(self):\n",
        "        self.name = input(\"Enter the name of the student : \")\n",
        "        self.ID = int(input(\"Enter the USN of the student : \"))\n",
        "        self.marks = []\n",
        "        for i in range(1, 4):\n",
        "            marks = input(f\"Enter the marks for subject {i} : \")\n",
        "            self.marks.append(marks)\n",
        "\n",
        "    def getData(self):\n",
        "        print(f\"Name : {self.name} \\nUSN : {self.ID} \\nMarks : \\nSubject 1 : {self.marks[0]} \\nSubject 2 : {self.marks[1]} \\nSubject 3 : {self.marks[2]}\")\n",
        "        return self.name, self.ID, self.marks\n",
        "\n",
        "s1 = Records()\n",
        "s1.setData()\n",
        "list1 = s1.getData()\n",
        "print(list1)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the name of the student : veekshith\n",
            "Enter the USN of the student : 2146\n",
            "Enter the marks for subject 1 : 60\n",
            "Enter the marks for subject 2 : 76\n",
            "Enter the marks for subject 3 : 80\n",
            "Name : veekshith \n",
            "USN : 2146 \n",
            "Marks : \n",
            "Subject 1 : 60 \n",
            "Subject 2 : 76 \n",
            "Subject 3 : 80\n",
            "('veekshith', 2146, ['60', '76', '80'])\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "q0xxgvpvaRWd"
      },
      "source": [
        "6"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uphi_wZRX_Pw",
        "outputId": "a9f60356-545e-4274-c207-5faf296bf234"
      },
      "source": [
        "class Time:\n",
        "    def setToDefault(self):\n",
        "        self.hours = 0\n",
        "        self.minutes = 0\n",
        "        self.seconds = 0\n",
        "\n",
        "    def setToVal(self, hours, minutes, seconds):\n",
        "        if seconds > 59:\n",
        "            tempMinutes = seconds // 60\n",
        "            seconds = seconds % 60\n",
        "            self.seconds = seconds\n",
        "            self.minutes = tempMinutes + minutes\n",
        "        else:\n",
        "            self.seconds = seconds\n",
        "            self.minutes = minutes\n",
        "\n",
        "        if self.minutes > 59:\n",
        "            tempHours = self.minutes // 60\n",
        "            self.minutes = self.minutes % 60\n",
        "            self.hours = tempHours + hours\n",
        "        else:\n",
        "            self.minutes = minutes\n",
        "            self.hours = hours\n",
        "\n",
        "    def displayTime(self):\n",
        "        print(f\"Time : {self.hours}::{self.minutes}::{self.seconds}\")\n",
        "\n",
        "\n",
        "T1 = Time()\n",
        "T1.setToDefault()\n",
        "T1.displayTime()\n",
        "T1.setToVal(10, 60, 60)\n",
        "T1.displayTime()\n",
        "T1.setToVal(10, 120, 150)\n",
        "T1.displayTime()\n",
        "T1.setToVal(10, 120, 60)\n",
        "T1.displayTime()"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Time : 0::0::0\n",
            "Time : 11::1::0\n",
            "Time : 12::2::30\n",
            "Time : 12::1::0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xQTQoJBYaS9N"
      },
      "source": [
        "7"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LrWFhs2uYaUI",
        "outputId": "2307e8c9-4984-47c7-adcb-c6e3267eeb11"
      },
      "source": [
        "class Student:\n",
        "    def __init__(self, name, age, rollNo):\n",
        "        self.name = name\n",
        "        self.age = age\n",
        "        self.rollNo = rollNo\n",
        "\n",
        "    @classmethod\n",
        "    def compareStudentsAge(cls, std1, std2):\n",
        "        if std1.age == std2.age:\n",
        "            print(\"Age of the students are equal.\")\n",
        "        else:\n",
        "            print(\"Age of the students are not equal.\")\n",
        "\n",
        "std1 = Student(\"Arjun\", 21, 43)\n",
        "std2 = Student(\"vyrum\", 20, 94)\n",
        "\n",
        "Student.compareStudentsAge(std1, std2)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Age of the students are not equal.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "x4oTNn4uaUR9"
      },
      "source": [
        "8"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "c4h0aC4BYpzx",
        "outputId": "e966a7fd-daf8-46cc-db0a-a9a86f3273cb"
      },
      "source": [
        "class Student:\n",
        "    sem = 3\n",
        "    institute = \"IIIT Dharwad\"\n",
        "    \n",
        "    def setData(self):\n",
        "        self.name = input(\"Enter the name of the student : \")\n",
        "        self.id = int(input(\"Enter the USN of student : \"))\n",
        "\n",
        "    def getInstanceData(self):\n",
        "        print(f\"Name : {self.name} \\nUSN = {self.id}\")\n",
        "\n",
        "    @classmethod\n",
        "    def getClassData(cls):\n",
        "        print(f\"Semester : {cls.sem} \\nInstitute : {cls.institute} \\n\")\n",
        "\n",
        "    @staticmethod\n",
        "    def getExplanation():\n",
        "        print(\"Class variables namely sem and institute are printed using ClassMethod and Instance variables namely name and id are printed using Instance Method\")\n",
        "\n",
        "\n",
        "s1 = Student()\n",
        "s1.setData()\n",
        "s1.getInstanceData()\n",
        "Student.getClassData()\n",
        "Student.getExplanation()"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the name of the student : harsha\n",
            "Enter the USN of student : 04\n",
            "Name : harsha \n",
            "USN = 4\n",
            "Semester : 3 \n",
            "Institute : IIIT Dharwad \n",
            "\n",
            "Class variables namely sem and institute are printed using ClassMethod and Instance variables namely name and id are printed using Instance Method\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "83SFIeoiY2jB",
        "outputId": "80d261ff-8d4b-470d-e1ed-f0af5ee302df"
      },
      "source": [
        "class Student:\n",
        "    def setData(self):\n",
        "        self.Name = input(\"Enter the name : \")\n",
        "        self.ID = int(input(\"Enter the Roll Number : \"))\n",
        "        self.sem = int(input(\"Enter the semester number : \"))\n",
        "        self.nLaptop = int(input(\"Enter the number of laptops : \"))\n",
        "        self.listLaptop = []\n",
        "        for i in range (0, self.nLaptop):\n",
        "            tempObj = self.Laptop()\n",
        "            self.listLaptop.append(tempObj)\n",
        "\n",
        "    class Laptop:\n",
        "        def __init__(self):\n",
        "            self.cpu = input(\"Enter the name of the CPU : \")\n",
        "            self.ram = input(\"Enter the RAM of the Laptop : \")\n",
        "            self.hardDisk = input(\"Enter the size of hard disk : \")\n",
        "            self.display = input(\"Enter the display resolution : \")\n",
        "        \n",
        "        def getData(self):\n",
        "            print(f\"\\nCPU : {self.cpu} \\nRAM : {self.ram} \\nHard Disk : {self.hardDisk} \\nDisplay Resolution : {self.display} \\n\")\n",
        "\n",
        "    def getData(self):\n",
        "        print(f\"\\nName : {self.Name} \\nUSN : {self.ID} \\nSemester : {self.sem} \\nNumber of Laptops : {self.nLaptop}\")\n",
        "        for i in range(0, self.nLaptop):\n",
        "            print(f\"Details of {i+1}th laptop : \")\n",
        "            self.listLaptop[i].getData()\n",
        "\n",
        "S1 = Student()\n",
        "S1.setData()\n",
        "S1.getData()"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter the name : virat\n",
            "Enter the Roll Number : 24\n",
            "Enter the semester number : 2\n",
            "Enter the number of laptops : 1\n",
            "Enter the name of the CPU : 1\n",
            "Enter the RAM of the Laptop : 8\n",
            "Enter the size of hard disk : 128\n",
            "Enter the display resolution : 360\n",
            "\n",
            "Name : virat \n",
            "USN : 24 \n",
            "Semester : 2 \n",
            "Number of Laptops : 1\n",
            "Details of 1th laptop : \n",
            "\n",
            "CPU : 1 \n",
            "RAM : 8 \n",
            "Hard Disk : 128 \n",
            "Display Resolution : 360 \n",
            "\n"
          ]
        }
      ]
    }
  ]
}