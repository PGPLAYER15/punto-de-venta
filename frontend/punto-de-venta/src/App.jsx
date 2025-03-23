import './App.css'
import Login from './pages/login/login'
import Signup from './pages/singup/Signup'
import { BrowserRouter, Routes, Route } from "react-router-dom";


function App() {

  return (
    <>
    <BrowserRouter>
      <Routes>
        <Route path="/Login" element={<Login/>} />
        <Route path="/Crearcuenta" element={<Signup/>} />
      </Routes>
    </BrowserRouter>

    </>
  )
}

export default App
