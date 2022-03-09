import Navbar from "./Navbar";
import { ArrowCircleRightIcon } from "@heroicons/react/solid";
import axios from 'axios';
import { useEffect, useState } from "react";
import { Popover } from '@headlessui/react'

const ViewStudentList = () => {
    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";

    const [listOfStudents, setListOfStudents] = useState([])

    useEffect(() => {
        axios({
            method: "get",
            url: "http://127.0.0.1:8080/api/students",
            headers: {
				Authorization : 'Token ' + localStorage.getItem("Token")
			}
        })
            .then((res) => setListOfStudents(res.data))
            .catch((err) => console.error(err))
        
        
    }, [])

    const listItem = listOfStudents.reverse().map((listOfStudents) => (
        <div className="flex justify-between">
            {`${listOfStudents.first_name} ${listOfStudents.last_name} ${listOfStudents.rollno}`}
        </div>
    ));

    return (
        <div className="flex flex-col h-screen">
            <Navbar />
            {listItem}
        </div>
    );
};

export default ViewStudentList;
