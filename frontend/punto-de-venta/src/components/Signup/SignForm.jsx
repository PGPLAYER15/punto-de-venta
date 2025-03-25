import InputField from '../InputField/InputField';
import { StyledWrapper } from '../Login/Loginstyle';
import { Link, Outlet } from 'react-router-dom';
import { useCliente } from '../../hooks/useCliente';

const SignForm = () => {
    const { 
        nombre, 
        setNombre, 
        email, 
        setEmail, 
        password, 
        setPassword, 
        confirmPassword, 
        setConfirmPassword, 
        handlecrearCliente 
    } = useCliente();

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (password !== confirmPassword) {
            console.log('Las contraseñas no coinciden');
            return;
        }
    
        try {
            const response = await handlecrearCliente(nombre, email, password);
            console.log('Formulario enviado:', response);
        } catch (e) {
            console.error('Error al enviar el formulario:', e);
        }
    };

    return (
        <StyledWrapper>
            <form className="form" onSubmit={handleSubmit}>
                <InputField 
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)} 
                    label="Email" 
                    type="email" 
                    name="email" 
                    id="email" 
                />
                <InputField 
                    value={nombre} 
                    onChange={(e) => setNombre(e.target.value)} 
                    label="Username" 
                    type="text" 
                    name="username" 
                    id="username" 
                />
                <InputField 
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)} 
                    label="Password" 
                    type="password" 
                    name="password" 
                    id="password" 
                />
                <InputField 
                    value={confirmPassword} 
                    onChange={(e) => setConfirmPassword(e.target.value)} 
                    label="Confirm Password" 
                    type="password" 
                    name="confirmPassword" 
                    id="confirmPassword" 
                />
                <button className="submit" type="submit">Registrate</button>
                <span className="span">
                    Tienes cuenta? <Link to="/Login">Iniciar Sesion</Link>
                </span>
            </form>
            <Outlet />
        </StyledWrapper>
    );
};

export default SignForm;