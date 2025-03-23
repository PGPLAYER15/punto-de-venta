import InputField from '../InputField/InputField';
import { StyledWrapper } from '../Login/Loginstyle';
import { Link, Outlet } from 'react-router-dom';

const SignForm = () => {
    return (
        <StyledWrapper>
            <form className="form">
                <InputField label="Email" type="email" name="email" id="email" />
                <InputField label="Username" type="user" name="username" id="username" />
                <InputField label="Password" type="password" name="password" id="password" />
                <InputField label="Confirm Password" type="password" name="confirmPassword" id="confirmPassword" />
                <input className="submit" type="submit" defaultValue="Sign up" />
                <span className="span">
                    Tienes cuenta? <Link to="/Login">Iniciar Sesion</Link>
                </span>
            </form>
            <Outlet/>
        </StyledWrapper>
    );
}

export default SignForm;