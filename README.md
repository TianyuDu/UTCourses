# UTCourses
Web scraping and retrieve course information from terminal

## Bash Version
The entire implementation is in `./core.sh`. The only dependency is `jq` package, which should be pre-installed on most Mac and Linux machines.

### Example Usage
1. Copy the `ut()` function in it to `~/.bash_profile` (or other locations your shell has access to).
2. Restart shell.
3. Run `ut eco499` in terminal:
```
ECO499H1-Y-20199 Honours Essay in Applied Microeconomics
Enrollment Info
prerequisite: ECO200Y1/ECO204Y1/ECO206Y1; ECO202Y1/ECO208Y1/ECO209Y1; ECO220Y1/ECO227Y1/ (STA220H1, STA255H1)/ (STA237H1, STA238H1)/ (STA257H1, STA261H1); ECO372H1/ECO374H1/ECO375H1; 3.0 GPA in economics courses; approval of the Associate Chair, Undergraduate
corequisite:
exclusion:
breadthCategories: Society and its Institutions (3)
Section: LEC-0101
Instructor: A Siow
[ WE ] 14:00 ~ 17:00 @ OI 2199 & OI 2281
**********************END***********************
```

## Python Version
Use `./download_info.py` to scrap information from timetable.

Use `./read_info.py` to print information in terminal.
