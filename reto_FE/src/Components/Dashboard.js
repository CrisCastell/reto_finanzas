import React, {useEffect, useState} from 'react'
import { authenticatedAxios } from './axios'

function Dashboard() {
    const [creditoID, setCreditoID] = useState(null)
    const [creditos , setCreditos ] = useState([])
    const [credito  , setCredito ] = useState({})
    // const [aprobados, setAprobados] = useState([])
    const [errorCreditos    , setErrorCreditos    ] = useState(false)
    const [errorDetail    , setErrorDetail    ] = useState(false)
    const [errorMessage, setErrorMessage] = useState('')
    const [loadingCreditos  , setLoadingCreditos  ] = useState(false)
    const [loadingDetail  , setLoadingDetail  ] = useState(false)
    const [array, setArra] = useState(['uno', 'dos', 'tres'])
    

    useEffect(()=>{
        getCreditosAction()
    }, [])

    useEffect(()=>{
        if(Object.keys(credito).length === 0){
            getCreditosAction()
        }
    }, [credito])

    useEffect(()=>{
        if(creditoID !== null){
            getCreditoDetailAction(creditoID)
        }
    }, [creditoID])


    const handleDecision = (e) => {
        const decision = e.target.id
        const newData = {aprobado:false, denegado:false}

        if(decision === 'aprobar'){
            newData.aprobado = true
        } else {
            newData.denegado = true
        }

        enviarDatosAction(credito.id, newData)
        
    }



    const enviarDatosAction = async (creditoID, data) => {

        setLoadingDetail(true)
        try{
            const response = await authenticatedAxios.put(`credito/decision/${creditoID}`, data)
            console.log(response)
            setLoadingDetail(false)
            setCredito({})

        } catch (error) {
            const message = 'Lo sentimos, hubo un error'
            setErrorDetail(true)
            setErrorMessage(message)
            setLoadingDetail(false)
        }
        
    }

    const getCreditosAction = async () => {

        setLoadingCreditos(true)
        try{
            const response = await authenticatedAxios.get(`creditos`)
            console.log(response)
            setLoadingCreditos(false)
            setCreditos(response.data)

        } catch (error) {
            const message = 'Lo sentimos, hubo un error'
            console.log(error)
            setErrorCreditos(true)
            setErrorMessage(message)
            setLoadingCreditos(false)
        }
        
    }

    const getCreditoDetailAction = async () => {

        setLoadingDetail(true)
        try{
            const response =  await authenticatedAxios.get(`credito/${creditoID}`)
            console.log(response)
            setLoadingDetail(false)
            setCredito(response.data)

        } catch (error) {
            const message = 'Lo sentimos, hubo un error'
            setErrorDetail(true)
            setErrorMessage(message)
            setLoadingDetail(false)
        }
        
    }

    return (
        <div className="container">
            <h1>Finanzas App</h1>
            <div className="row">
                <div className="col-md-6">
                    { creditos.map(cred => 
                        
                        <div className="credito-bar container-fluid d-flex border border-dark" onClick={() => setCreditoID(cred.id) } id={cred.id}>
                            <p>{cred.nombre_empresa}</p>
                            <span>USD {cred.monto}</span>
                        </div>
                    )}
                    
                </div>
                <div className="col-md-6">
                    <div className="credito-detail">
                        
                        { 'id' in credito && !errorDetail && !loadingDetail ?
                        
                            <div>
                                <h2>Detalles de solicitud de credito</h2>
                                <div className="logo rounded-circle"><p>Logo de la empresa</p></div>
                                <p><strong>Monto del credito:</strong> {credito.monto} </p>
                                <p><strong>Monto total deuda la SBS:</strong> {credito.deudaSBS} </p>
                                <p><strong>Puntuacion Sentinel:</strong> {credito.puntuacionSentinel} </p>
                                <p><strong>Puntaje referencia:</strong> {credito.puntuacionIA}</p>
                                <div className="btns-box container">
                                    <button className="btn btn-success" onClick={handleDecision} name="aprobar" id="aprobar">Aprobar</button>
                                    <button className="btn btn-danger" onClick={handleDecision} name="denegar" id="denegar">Denegar</button>
                                </div>
                            </div>
                        
                        : 
                        
                        <div className="default-box">
                            <p className="default-text">Selecciona uno de los creditos de la lista para verlo en detalle.</p>
                        </div>

                        }
                    </div>
                    
                </div>
            </div>
        </div>
    )
}

export default Dashboard
