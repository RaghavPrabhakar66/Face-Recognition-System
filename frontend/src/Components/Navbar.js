import { MenuIcon, HomeIcon, UserAddIcon, LogoutIcon } from "@heroicons/react/solid";
import { Menu, Transition } from '@headlessui/react'
import { Link } from "react-router-dom";


const Navbar = () => {
	return (
		<div>
			<div className="navbar mb-2 shadow-lg bg-blue-500 text-neutral-content ">
				<div className="flex-1 px-2 mx-2">
					<span className="text-lg font-bold">
						Thapar Attendence System
					</span>
				</div>
			</div>
			<div className="absolute right-0 top-0 p-2 z-20">
				<Menu>
					<Menu.Button className="ml-32">
						<button className="btn btn-square btn-ghost">
							<MenuIcon className="h-8 w-8" />
						</button>
					</Menu.Button>

					<Menu.Items className="flex flex-col space-y-2 mt-4 bg-slate-200 rounded-lg p-2 divide-y w-44">
						<Link to="/dashboard">
							<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 rounded-lg">
								{({ active }) => (

									<div
										className={`${active && 'bg-blue-500 flex flex-col'}`}
									>
										<HomeIcon className="h-5 w-5 mr-1" />
										Home
									</div>

								)}
							</Menu.Item>
						</Link>
						<Link to="/add-student">
							<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 rounded-lg">
								{({ active }) => (
									<div
										className={`${active && 'bg-blue-500'}`}
									>
										<UserAddIcon className="h-5 w-5 mr-1" />
										Add Student
									</div>
								)}
							</Menu.Item>
						</Link>
						<Link to="/login">
							<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 rounded-lg">
								{({ active }) => (

									<div
										className={`${active && 'hover'}`}

									>
										<LogoutIcon className="h-5 w-5 mr-1" />
										Log out
									</div>
								)}
							</Menu.Item>
						</Link>
					</Menu.Items>

				</Menu>
			</div>
		</div >
	);
};

export default Navbar;