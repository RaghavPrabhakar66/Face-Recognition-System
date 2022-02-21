import Navbar from "./Navbar";
import { UserAddIcon } from "@heroicons/react/solid";
import { Link } from "react-router-dom";

const Dashboard = () => {
	return (
		<div className="flex flex-col h-screen">
			<Navbar />
			<footer className="absolute bottom-5 right-5 z-10">
				<Link to="/add-student">
					<button className="flex h-20 w-20 bg-blue-200 rounded-full transition-all active:w-[4.9rem] active:h-[4.9rem] active:bg-blue-100">
						<UserAddIcon className="h-10 w-10 m-auto" />
					</button>
				</Link>
			</footer>
		</div>
	);
};

export default Dashboard;
