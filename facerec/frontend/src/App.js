import "./App.css";
import Login from "./Components/Login";
import SignUp from "./Components/SignUp";
import Dashboard from "./Components/Dashboard";
import AddStudent from "./Components/AddStudent";
import Test from "./Components/test";
import ModifyStudent from "./Components/ModifyStudent";
import DeleteStudent from "./Components/DeleteStudent";
import ViewStudentList from "./Components/ViewStudentList"
import {
	BrowserRouter as Router,
	Routes,
	Route,
	Navigate,
} from "react-router-dom";


function App() {
	return (
		<div>
			<Router>
				<Routes>
					<Route
						exact
						path="/"
						element={<Navigate replace to="/site/login" />}
					/>
					<Route exact path="/site">
						<Route path="login" element={<Login />} />
						<Route path="signup" element={<SignUp />} />
						<Route path="dashboard" element={<Dashboard />} />
						<Route path="add-student" element={<AddStudent />} />
						<Route path="modify-student" element={<ModifyStudent />}/>
						<Route path="delete-student" element={<DeleteStudent />}/>
						<Route path="view-student" element={<ViewStudentList />}/>
						<Route path="test" element={<Test />} />
					</Route>
				</Routes>
			</Router>
		</div>
	);
}

export default App;
