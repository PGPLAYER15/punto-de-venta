import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

// Crear un cliente

export const crearCliente = async (nombre, email,password) => {
    try {
        const responsemail = await axios.get(`${API_URL}/clientes/email/${email}`);

        if (responsemail.data) {
            console.log('Ese correo ya está registrado');
            return null; // Cliente ya existe
        }
        
    } catch (error) {
        if (error.response && error.response.status === 404) {
            // Si el cliente no existe, proceder a crearlo
            const response = await axios.post(`${API_URL}/clientes`, {
                nombre: nombre,
                email: email,
                password: password
            });
            return response.data;
        }
        console.error('Error al verificar el cliente:', error);
        throw error;
    }
}

export const updateCliente = async (id, nombre, email, tarjeta) => {

    try {
        const response = await axios.put(`${API_URL}/clientes/${id}`, {
            nombre: nombre,
            email: email,
            tarjeta: tarjeta
        });
        return response.data;
    } catch (error) {
        console.error('Error al actualizar el cliente:', error);
        throw error;
    }
}

export const loginCliente = async (email, password) => {

    try {

        const response = await axios.get(`${API_URL}/login/`,{
            email: email,
            password: password
        });

        if(password == response.data.password){
            console.log('Cliente logueado:', response.data);
        }
        
        return console.log('Contraseña incorrecta');
        
    } catch (error) {
        console.error('Error al iniciar sesión:', error);
        throw error;
    }
    
}