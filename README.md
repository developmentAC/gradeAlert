##### Grade-Alert:
##### Date: 11 Sept 2021
##### Oliver Bonham-Carter, [Allegheny College](https://allegheny.edu/)
##### email: obonhamcarter@allegheny.edu

---

![logo](graphics/gradeAlert_logo.png)

[![MIT Licence](https://img.shields.io/bower/l/bootstrap)](https://opensource.org/licenses/MIT)

[![BLM](https://img.shields.io/badge/BlackLivesMatter-yellow)](https://blacklivesmatter.com/)

GitHub link: https://github.com/developmentAC/beagleTM

### Table of contents
* [Overview](#overview)
* [Tool](#tool)
* [Usage-At-Terminal](#usage-at-terminal)
* [CSV files](csv-files)
* [Outputted files](outputted-files)
* [Pushing in Bulk](pushing-in-bulk)
* [A work in progress](A-work-in-progress)



### Overview
GitHub Classroom is an excellent resource to handle work repositories for a course of many students. Each student, after "accepting" an assignment is issued a unique repository in which work can be completed and pushed to the instructor.

Here, we suggest that GitHub Classroom be used to report grades to each student who has a grade book "assignment" repository. The instructor, who has access to this repository, places a file containing grades and feedback into this repository for the student to consult.

![Demo](graphics/gradeAlert_demo.gif)


### Tool

All grades in a course are kept in a CSV spreadsheet. Grade-alert parses each row of the  spreadsheet and all contents are formatted and placed into a separate markdown file which is named according to the first column of the spreadsheet. These files are then to be placed into grade book repositories (discussed below) and pushed for the student to access.


### Usage-At-Terminal

To run the program in Linux or MacOS, Python3 is necessary. This program is sure to also run in Windows, although this has not been tested.

To process the CSV spreadsheet, `demoGrades_short.csv` (files formats are discussed below), the command is the following: `./gradeAlert.py demoGrades_short.csv`. In addition, online help is available by at the terminal with the command, `./gradeAlert.py -h`.




### CSV files

To use this Grade-Alert, the student grades are to be kept in a comma separated variable (CSV) file. Please note that no commas may be used in the fields of the CSV file as they will serve to confuse the true delimiters of the CSV structure and will prevent Grade-Alert from opening the CSV files correctly.



In a grade book spreadsheet, each row contains the grades of a particular individuals in the course. The columns header provide details of the assignment and type of feedback. The first column **must** contain the name of the student; this information will be used to name the outputted files and serve to inform which output file corresponds with what grade book repository. The rest of the information for a row will be formatted and placed into the outputted file. The CSV formatting for a grade book CSV files is shown below in the table.


|Student Name|	Student ID|	Activity 01|	Activity 01 Comments|	Activity 02|	Activity 02 comments|
|---|---|---|---|---|---|
|student1|	x0001|	100|	All requirements satisfied|	100|	excellent|
|student2|	x0002|	100|	Excellent|	100|	excellent|
|student3|	x0003|	100|	Excellent|	100|	excellent|
|student4|	x0004|	0|	Nothing submitted|	95|	excellent|
|student5|	x0005|	100|	Excellent|	95|	nothing submitted?|
|student6|	x0006|	100|	Excellent|	100|	excellent|
|student7|	x0007|	0|	Nothing submitted|	0|	nothing submitted?|

### Outputted files

After running the Grade-Alert tool on a CSV file containing the information of the above table, a file for each row is outputted. For example, the report of `student1` will take the following form.


File: `student1_gradebook.md`

```
Student Name : student1

Student ID : x0001

Activity 01 : 100

Activity 01 Comments : All requirements satisfied

Activity 02 : 100

Activity 02 comments : excellent

Activity 03 : 100

Activity 03 comments : yes


____

```

Each prepared file is to be then to be placed into its associated grade book repository and is pushed out for the student.



### Pushing in Bulk

Each student who has accepted the grade book "assignment" will have a repository that the instructor can access. The instructor will then use [GitHub Assistant](http://https://classroom.github.com/assistant) (link: https://classroom.github.com/assistant) to create a local directory containing all cloned grade book repositories.

After completing course grades and saving them in a CSV file, Grader-Alert may be executed with the CSV file as the parameter. The resulting files will have to be placed into the individual grade book repositories. To facilitate the pushing of all these repositories, the below script (located in `src/bulkPusher.sh`) may be be used. To execute this script in Linux and MacOS, use the command, `sh bulkPusher.sh` when the files have been copied into the grade book repositories.




```bash

# Bulk Pusher script.
# Date: 11 Sept 2021
# Oliver Bonham-Carter, obonhamcarter@allegheny.edu
# This script uses the file, dirNames to locate repositories to push
# The current date is printed in the commit message of the submit
# A file, "0_thisLastPush.txt" is created to state when the last bulk push was completed.


NOW=`date`
printf "Current date and time in Linux is: $NOW"

date > 0_thisLastPush.txt

pwd > mydir
for z in `cat mydir`; do cd $z; done
for DIRNAME in $(cat dirNames)
do
    cd $DIRNAME
    echo Checking: $DIRNAME
     git add -A
     git commit -m "Grade update: $NOW"
     git push
    cd $z/
done

rm mydir


```

The file, `dirNames` contains the paths of the repositories to which we push.




![Titles may be found in the networks, File mouseOver.png](graphics/mouseOver.png)
Figure 1: A screenshot.





### A work in progress

Check back often to see the evolution of this project!! Grade-Alert is a work-in-progress. Updates are likely to come soon with feedback. If you would like to contribute to this project, __then please do!__ For instance, if you see some low-hanging fruit or task that you could easily complete, that could add value to the project, then I would love to have your insight.

Otherwise, please create an Issue for bugs or errors. Since I am a teaching faculty member at Allegheny College, I may not have all the time necessary to quickly fix the bugs and so I would be very happy to have any help that I can get from the OpenSource community for any technological insight. Much thanks in advance. I hope that this project helps you find the knowledge from PubMed that you require for your project. :-)
