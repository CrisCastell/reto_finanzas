import axios from 'axios'

export const authenticatedAxios = axios.create({
    baseURL: 'http://127.0.0.1:8000/api/finanzas/',
    headers: {
        'Authorization': `Token 223553b9d26b9ae24cf57bcd31fc7478d373e084`
    }
});