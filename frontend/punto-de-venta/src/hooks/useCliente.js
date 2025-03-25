import {useState} from 'react';
import {crearCliente , updateCliente} from '../services/ClientService';

export const useCliente = () => {

    const [nombre, setNombre] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');


    const [error , setError] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handlecrearCliente = async (nombre, email, password) => {

        setIsLoading(true);
        setError(null);

    
        try {
            const response = await crearCliente(nombre, email, password);
            if (response) {
                console.log('Cliente creado', response);
                return response;
            } else {
                return null;
            }
        } catch (error) {
            setError('Error al crear el cliente. Por favor, inténtalo de nuevo.');
            console.error(error);
            return null;
        } finally {
            setIsLoading(false);
        }
    };

    const handleUpdateUser = async(id, nombre,email,tarjeta) => {

        setIsLoading(true);
        setError(null);

        try{

            const actualizarCliente = await updateCliente(id,nombre,email,tarjeta);
            console.log("Cliente actualizado:", actualizarCliente);

        }catch(error){
            setError('Error al actualizar el cliente. Por favor, inténtalo de nuevo.');
            console.error(error);
        }

    }

    const handleLogin = async (email, password) => {
        try {
            const cliente = await loginCliente(email, password);
            console.log('Cliente logueado:', cliente);
        }catch(error){
            console.error('Error al iniciar sesión:', error);
        }
    }



    return {
        nombre,
        setNombre,
        email,
        setEmail,
        password,
        setPassword,
        confirmPassword,
        setConfirmPassword,
        error,
        isLoading,
        handlecrearCliente,
        handleUpdateUser,
        handleLogin
    }
}
