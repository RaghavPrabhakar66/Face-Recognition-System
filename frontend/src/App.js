import "./App.css";
import Login from "./Components/Login";
import SignUp from "./Components/SignUp";
import Dashboard from "./Components/Dashboard";
import AddStudent from "./Components/AddStudent";
import Test from "./Components/test";
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
						<Route path="test" element={<Test />} />
					</Route>
				</Routes>
			</Router>
		</div>
	);
}

export default App;
