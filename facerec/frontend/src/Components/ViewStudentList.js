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
                Authorization: 'Token ' + localStorage.getItem("Token")
            }
        })
            .then((res) => setListOfStudents(res.data))
            .catch((err) => console.error(err))


    }, [])

    const listItem = listOfStudents.reverse().map((listOfStudents) => (
        <tr>
            <td>{`${listOfStudents.id}`}</td>
            <td>{`${listOfStudents.first_name}`}</td>
            <td>{`${listOfStudents.last_name}`}</td>
            <td>{`${listOfStudents.rollno}`}</td>
        </tr>
    ));

    const orderItem = listItem.sort((a,b) => (
        a.rollno > b.rollno ? 1 : -1
    ))
    return (
        <div className="flex flex-col h-screen">
            <Navbar />
            <table className='table-auto w-1/2 bg-white/[0.12] mx-auto'>
                <thead>
                    <tr>
                        <th>Id</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Roll Number</th>
                    </tr>
                </thead>
                <tbody>
                    {listItem}
                </tbody>
            </table>
        </div>
    );
};

export default ViewStudentList;
