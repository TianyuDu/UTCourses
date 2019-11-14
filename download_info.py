import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
import time


class bot():
    def __init__(self):
        self.driver = webdriver.Chrome("/Users/tianyudu/Downloads/ut_courses/chromedriver")
        self.driver.get("https://timetable.iit.artsci.utoronto.ca/")

    def close(self):
        self.driver.close()

    def batch_retrive(self, department: str) -> pd.DataFrame:
        department = department.upper()
        search_box = self.driver.find_element_by_id("courseCode")
        search_button = self.driver.find_element_by_id("searchButton")
        search_box.clear()
        search_box.click()
        search_box.send_keys(department)
        search_button.click()
        course_lst = []
        while course_lst == []:
            time.sleep(1.0)
            course_lst = self.driver.find_elements_by_class_name("perCourse")

        course_info_lst = []
        print(f"Total courses found: {len(course_lst)}")
        for course in course_lst:
            code, title = course.find_element_by_class_name("courseTitle").text.split("   ")
            print(f"{code}\t{title}")
            meeting_lst = course.find_elements_by_class_name("perMeeting")
            for meeting in meeting_lst:
                meeting_code = meeting.find_element_by_class_name("colCode").text
                print(f"\t{meeting_code}")
                try:
                    meeting_info = meeting.find_element_by_class_name(
                        "secLec" if meeting_code.startswith("LEC") else "secTut").text
                except selenium.common.exceptions.NoSuchElementException:
                    meeting_info = meeting.find_element_by_class_name("secPra").text
                info = [code, title, meeting_code, meeting_info]
                course_info_lst.append(info)
        course_info_df = pd.DataFrame(
            np.array(course_info_lst),
            columns=["Code", "Title", "Session", "Details"]
        )
        return course_info_df

    def batch_download(self, save_dir: str) -> None:
        department_lst = [
            x.text
            for x in self.driver.find_elements_by_class_name("option")
        ]
        print(department_lst)

        code_lst = [
            x[1:-1]
            for dep in department_lst
            for x in dep.split(" ")
            if x.startswith("(") and x.endswith(")")
        ]

        # code_lst = ["CSC", "MAT", "ECO", "STA"]
        code_lst = ["MAT"]

        all_courses = []
        for x in code_lst:
            y = self.batch_retrive(x)
            all_courses.append(y)
        df = pd.concat(all_courses, axis=0)
        print(df.head())
        print(df.shape)
        df.to_csv(save_dir)


if __name__ == "__main__":
    b = bot()
    b.batch_download(save_dir="./MAT.csv")
    b.close()
