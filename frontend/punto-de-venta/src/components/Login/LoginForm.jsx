import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import { StyledWrapper } from './Loginstyle';
import InputField from '../InputField/InputField';

const LoginForm = () => {
  return (
    <StyledWrapper>
      <form className="form">
        <InputField label="Email" type="email" name="email" id="email" />
        <InputField label="Password" type="password" name="password" id="password" />
        <span className="span">
          <a href="#">Forgot password?</a>
        </span>
        <input className="submit" type="submit" defaultValue="Log in" />
        <span className="span">
          Aun no tienes cuenta? <Link to="/Crearcuenta">Crear cuenta</Link>
        </span>
      </form>
      <Outlet />
    </StyledWrapper>
  );
};

export default LoginForm;