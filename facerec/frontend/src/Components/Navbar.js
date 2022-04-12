import { MenuIcon, HomeIcon, UserAddIcon, LogoutIcon, TrashIcon, DocumentIcon } from "@heroicons/react/solid";
import { Menu } from '@headlessui/react'
import { Link } from "react-router-dom";
import logo from '../Images/thapar.png';

const Navbar = () => {

	async function logout() {
		localStorage.removeItem('Token');
	}

	return (
		<div>
			<div className="navbar mb-2 shadow-lg text-neutral-content max-h-10">
				<div className="flex-1 px-2 mx-2">
						<Link to='/site/dashboard'>
							<img src={logo} alt="TAS" className="h-14 w-14 mr-2"></img>
						</Link>
					<span className="text-lg font-bold text-black">
						<Link to='/site/dashboard'>
							Thapar Attendance System
						</Link>
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

					<Menu.Items className="flex flex-col space-y-2 mt-4 bg-slate-200 rounded-lg p-2 divide-y divide-slate-300 w-44">
						<div>
							<Link to="/site/dashboard">
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
						</div>
						<div className="flex flex-col space-y-1">
							<Link to="/site/add-student">
								<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 rounded-lg mt-1">
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
							<Link to="/site/modify-student">
								<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 rounded-lg">
									{({ active }) => (
										<div
											className={`${active && 'bg-blue-500'}`}
										>
											<DocumentIcon className="h-5 w-5 mr-1" />
											Modify Student
										</div>
									)}
								</Menu.Item>
							</Link>
							<Link to="/site/delete-student">
								<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 rounded-lg">
									{({ active }) => (
										<div
											className={`${active && 'bg-blue-500'}`}
										>
											<TrashIcon className="h-5 w-5 mr-1" />
											Delete Student
										</div>
									)}
								</Menu.Item>
							</Link>
						</div>
						<div>
							<Link onClick={logout} to="/site/login">
								<Menu.Item className="flex justify-start hover:bg-blue-200 p-1 mt-1 rounded-lg">
									{({ active }) => (

										<div
											className={`${active && 'hover'}`}

										>
											<LogoutIcon className="h-5 w-5 mx-1" />
											Log out
										</div>
									)}
								</Menu.Item>
							</Link>
						</div>
					</Menu.Items>

				</Menu>
			</div>
		</div >
	);
};

export default Navbar;
