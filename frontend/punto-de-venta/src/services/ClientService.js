import axios from 'axios';
const API_URL = 'http://127.0.0.1:8000';

// Crear un cliente


export const crearCliente = async (nombre, email, password) => {
    console.log(email)
    try {
        console.log(email)
        const responseemail = await axios.get(`${API_URL}/clientes/email/${email}`);
        if (responseemail.data) {
            console.log('El correo ya está registrado');
            return null;
        }
    } catch (error) {
        if (error.response && error.response.status === 404) {
            console.log("El correo no está registrado, continuando con el registro...");
        } else {
            console.error("Error al verificar el correo:", error);
            return null;
        }
    }
    
    try {
        console.log(email)
        const response = await axios.post(`${API_URL}/clientes/create`, {
            nombre:nombre,
            email:email,
            password:password
        });

        return response.data;
    } catch (error) {
        console.error("Error al crear el cliente:", error);
        return null;
    }
};

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
        const response = await axios.post(`${API_URL}/login/`, {
            email,
            password
        });

        return response.data;
    } catch (error) {
        console.error('Error al iniciar sesión:', error);
        throw error;
    }
};