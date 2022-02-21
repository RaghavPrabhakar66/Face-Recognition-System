import Navbar from "./Navbar";
import { UserAddIcon, ArrowCircleRightIcon } from "@heroicons/react/solid";
import { Link } from "react-router-dom";

const Dashboard = () => {
	return (
		<div className="flex flex-col h-screen">
			<Navbar />
			<div className="bg-slate-200 w-1/2 place-self-center rounded-lg p-2 space-y-5 ">
				<div className="flex justify-between">
					Student 1
					<button>
						<ArrowCircleRightIcon className="h-6 w-6" />
					</button>
				</div>
				<div className="flex justify-between">
					Student 2
					<button>
						<ArrowCircleRightIcon className="h-6 w-6" />
					</button>
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