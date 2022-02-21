import { MenuIcon } from "@heroicons/react/solid";

const Navbar = () => {
	return (
		<div className="navbar mb-2 shadow-lg bg-blue-500 text-neutral-content ">
			<div className="flex-1 px-2 mx-2">
				<span className="text-lg font-bold">
					Thapar Attendence System 
				</span>
			</div>
			<div className="flex-none">
				<button className="btn btn-square btn-ghost">
					<MenuIcon className="h-8 w-8" />
				</button>
			</div>
		</div>
	);
};

export default Navbar;
