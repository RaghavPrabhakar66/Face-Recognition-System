import Navbar from "./Navbar";
import { UserAddIcon, ArrowCircleRightIcon } from "@heroicons/react/solid";
import { Link } from "react-router-dom";
import axios from 'axios';
import { useState } from "react";
import { Popover } from '@headlessui/react'
import { Tab } from '@headlessui/react'


function classNames(...classes) {
	return classes.filter(Boolean).join(' ')
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
					<Popover.Panel className="absolute z-10 bg-red-100 rounded-lg p-5 transition-all duration-100">
						{`Time of entry: ${listOfStudents.date} ${listOfStudents.time}`}
					</Popover.Panel>
				</button>
			</Popover>
		</div>
	));


	return (
		<div className="flex flex-col h-screen">
			<Navbar />
			<div className="w-1/2 place-self-center rounded-lg p-2 space-y-5 ">
				<Tab.Group>
					<Tab.List className="flex bg-slate-600 justify-around p-2 rounded-lg">
						<Tab
							className={({ selected }) =>
								classNames(
									'w-1/3 py-2.5 text-sm leading-5 font-medium text-red-700 rounded-lg',
									'focus:outline-none focus:ring-2 ring-offset-2 ring-offset-slate-400 ring-white ring-opacity-60',
									selected
										? 'bg-white shadow'
										: 'text-red-100 hover:bg-white/[0.12] hover:text-white'
								)
							}
						>Student</Tab>
						<Tab
							className={({ selected }) =>
								classNames(
									'w-1/3 py-2.5 text-sm leading-5 font-medium text-red-700 rounded-lg',
									'focus:outline-none focus:ring-2 ring-offset-2 ring-offset-slate-400 ring-white ring-opacity-60',
									selected
										? 'bg-white shadow'
										: 'text-red-100 hover:bg-white/[0.12] hover:text-white'
								)
							}
						>Attendance</Tab>
					</Tab.List>
					<Tab.Panels>
						<Tab.Panel className="flex flex-col justify-between space-y-2">
							<Link to="/site/add-student"><button className="bg-slate-200 rounded-lg w-30 h-20 p-2 w-full">Add Student</button></Link>
							<button className="bg-slate-200 rounded-lg w-30 h-20 p-2"><Link to="/site/modify-student">Modify Student</Link></button>
							<button className="bg-slate-200 rounded-lg w-30 h-20 p-2 "><Link to="/site/delete-student">Delete Student</Link></button>
							<button className="bg-slate-200 rounded-lg w-30 h-20 p-2 "><Link to="/site/signup">View Student List</Link></button>
						</Tab.Panel>
						<Tab.Panel>
							<div className="flex flex-col space-y-5">
								{listItem}
								<div className="flex justify-between">
									Kabir Seth
									<Popover className="relative">
										<button>
											<Popover.Button>
												<ArrowCircleRightIcon className="h-6 w-6" />
											</Popover.Button>
											<Popover.Panel className="absolute z-10 bg-red-100 rounded-lg p-5 transition-all duration-100">
												{`Time of entry: 12:05:22 pm`}
											</Popover.Panel>
										</button>
									</Popover>
								</div>
							</div>
						</Tab.Panel>
					</Tab.Panels>
				</Tab.Group>
			</div>
			<footer className="absolute bottom-5 right-5 z-10">
				<Link to="/site/add-student">
					<button className="flex h-20 w-20 bg-red-200 rounded-full transition-all active:w-[4.9rem] active:h-[4.9rem] active:bg-red-100">
						<UserAddIcon className="h-10 w-10 m-auto" />
					</button>
				</Link>
			</footer>
		</div>
	);
};

export default Dashboard;
