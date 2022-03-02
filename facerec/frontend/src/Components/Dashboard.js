import Navbar from "./Navbar";
import { UserAddIcon, ArrowCircleRightIcon } from "@heroicons/react/solid";
import { Link } from "react-router-dom";
import axios from 'axios';
import { useState } from "react";
import { Popover } from '@headlessui/react'

const Buttons = () => {
	return (
		<div className="w-1/2 place-self-center rounded-lg my-2 p-2 flex justify-between">
			<button className="bg-green-100 rounded-lg flex p-2">Add Student</button>
			<button className="bg-blue-100 rounded-lg flex p-2">Modify Student</button>
			<button className="bg-red-100 rounded-lg flex p-2">Delete Student</button>
		</div>
	)
}


const Dashboard = () => {
	const [listOfStudents, setListOfStudents] = useState([])

	axios
		.get("http://127.0.0.1:8080/api/attendances")
		.then((res) => {
			setListOfStudents(res.data)
		})
		.catch((err) => console.error(err));

	const listItem = listOfStudents.reverse().map((listOfStudents) => (
		<div className="flex justify-between">
			{`${listOfStudents.student.first_name} ${listOfStudents.student.last_name}`}
			<Popover className="relative">
				<button>
					<Popover.Button>
						<ArrowCircleRightIcon className="h-6 w-6" />
					</Popover.Button>
					<Popover.Panel className="absolute z-10 bg-blue-100 rounded-lg p-5 transition-all duration-100">
						{`Time of entry: ${listOfStudents.date} ${listOfStudents.time}`}
					</Popover.Panel>
				</button>
			</Popover>
		</div>
	));


	return (
		<div className="flex flex-col h-screen">
			<Navbar />
			<Buttons />
			<div className="bg-slate-200 w-1/2 place-self-center rounded-lg p-2 space-y-5 ">
				<div className="flex flex-col space-y-5">
					{listItem}
				</div>
			</div>
			<footer className="absolute bottom-5 right-5 z-10">
				<Link to="/site/add-student">
					<button className="flex h-20 w-20 bg-blue-200 rounded-full transition-all active:w-[4.9rem] active:h-[4.9rem] active:bg-blue-100">
						<UserAddIcon className="h-10 w-10 m-auto" />
					</button>
				</Link>
			</footer>
		</div>
	);
};

export default Dashboard;
