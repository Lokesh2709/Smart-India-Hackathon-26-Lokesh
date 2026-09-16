import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Students from "./pages/Students";
import Recruiters from "./pages/Recruiters";
import Analytics from "./pages/Analytics";
import GovernmentJobs from "./pages/GovernmentJobs";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/students" element={<Students />} />
        <Route path="/recruiters" element={<Recruiters />} />
        <Route path="/analytics" element={<Analytics />} />
        <Route path="/jobs" element={<GovernmentJobs />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;