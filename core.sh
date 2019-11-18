#! /bin/bash

ut(){
    url='https://timetable.iit.artsci.utoronto.ca/api/20199/courses?org=&code='${1}'&section=&studyyear=&daytime=&weekday=&prof=&breadth=&online=&waitlist=&available=&title='
    # rm ./_course_cache.json
    curl -s $url >  ./_course_cache.json
    # data=`curl -s $url`
    course_lst="$(cat ./_course_cache.json | jq 'keys_unsorted[]')"

    for z in $course_lst; do
        # For each course
        echo '*********************BEGIN**********************'
        course_name=`echo ${z} | tr -d '"'`
        echo ${course_name} `cat ./_course_cache.json | jq '.'${z}'.courseTitle' | tr -d '"'`
        echo 'Enrollment Info'
        fields=(prerequisite corequisite exclusion breadthCategories)
        for field in ${fields[@]}; do
            # echo '=================='$field'=================='
            echo $field: `cat ./_course_cache.json | jq '.'${z}'.'${field} | tr -d '"'`
        done
        # For each meeting
        meeting_lst="$(cat ./_course_cache.json | jq .${z}.meetings | jq 'keys[]')"
        for m in ${meeting_lst[@]}; do
            echo "Section:" ${m} | tr -d '"'
            # Get instructor
            instructor_id="$(cat ./_course_cache.json | jq '.'${z}'.meetings.'${m}'.instructors' | jq 'keys[]')"
            instructor_info=`cat ./_course_cache.json| jq .${z}.meetings.${m}.instructors.${instructor_id}`
            echo 'Instructor:' `echo ${instructor_info} | jq ".firstName" | tr -d '"'` `echo ${instructor_info} | jq ".lastName" | tr -d '"'`
            # Get scheduled time table
            schedule_id_lst="$(cat ./_course_cache.json | jq '.'${z}'.meetings.'${m}'.schedule' | jq "keys[]")"
            for schedule_id in ${schedule_id_lst[@]}; do
                meeting_info=`cat ./_course_cache.json | jq '.'${z}'.meetings.'${m}'.schedule.'${schedule_id}`
                day=`echo ${meeting_info} | jq '.meetingDay' | tr -d '"'`
                start=`echo ${meeting_info} | jq '.meetingStartTime' | tr -d '"'`
                end=`echo ${meeting_info} | jq '.meetingEndTime' | tr -d '"'`
                loc1=`echo ${meeting_info} | jq '.assignedRoom1' | tr -d '"'`
                loc2=`echo ${meeting_info} | jq '.assignedRoom2' | tr -d '"'`
                echo '[' ${day} ']' ${start} '~' ${end} '@' ${loc1} '&' ${loc2}
            done
        done
        echo '**********************END***********************'
    done
    rm ./_course_cache.json
}