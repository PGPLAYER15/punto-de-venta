import InputField from '../InputField/InputField';
import { StyledWrapper } from '../Login/Loginstyle';
import { Link, Outlet } from 'react-router-dom';
import { useCliente } from '../../hooks/useCliente';

const SignForm = () => {

    const { nombre, setNombre, email, setEmail, error, isLoading, password,setPassword,confirmPassword, setConfirmPassword, handlecrearCliente } = useCliente();

    const handleSubmit = (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            console.log('Las contraseñas no coinciden');
            return;
        }
        try {
            
            handlecrearCliente(nombre,email,password);
            console.log('Formulario enviado');
        } catch (e) {
            error = 'Error al enviar el formulario';
            console.log(error);
        }
    };

    return (
        <StyledWrapper>
            <form className="form" onSubmit={handleSubmit}>
                <InputField value={email} onChange={(e) => setEmail(e.target.value)} label="Email" type="email" name="email" id="email" />
                <InputField value={nombre} onChange={(e) => setNombre(e.target.value)} label="Username" type="user" name="username" id="username" />
                <InputField value={password} onChange={(e) => setPassword(e.target.value)} label="Password" type="password" name="password" id="password" />
                <InputField value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} label="Confirm Password" type="password" name="confirmPassword" id="confirmPassword" />
                <button className="submit" type="submit" defaultValue="Sign up" >Registrate </button>
{/*                 <input className="submit" type="submit" defaultValue="Sign up" />
 */}
                <span className="span">
                    Tienes cuenta? <Link to="/Login">Iniciar Sesion</Link>
                </span>
            </form>
            <Outlet />
        </StyledWrapper>
    );
}

export default SignForm;