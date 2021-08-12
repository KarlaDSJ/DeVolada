import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';

/**
 * Inteface para los tipos de datos para poder registrarse
 */

export interface IRegistrar {

    msg:string; //mesnaje del JSON para ver si los datos son correctos
    
    //los datos del comprador

    correoC:string,
    nombreC:string,
    telefonoC : number,
    estadoC : string,
    ciudadC : string,
    coloniaC : string,
    cpC : string,
    calleC : string,
    numeroC : number

    //los datos del vendedor

    correoV:string,
    nombreV:string,
    telefonoV : number,
        estadoV : string,
        ciudadV : string,
        coloniaV : string,
        cpV : string,
        calleV : string,
        numeroV : number,
        tarjetaV : String
    
}

@Injectable({
    providedIn: 'root'
  })

/**
 *Clase del servicio de registrar para que el componente de registrar se pueda subscribirse  
*/

export class RegistrarService{
    
    private _url = 'http://127.0.0.1:5000/'; // la url del servidor para mandar las peticiones JSON
    
    /**
     * Constructor de las clase
     * @param _http el protocolo por el cual se van a enviar las peticiones
     */

    constructor(private _http: HttpClient){}

    /**
     * Metodo para mandar los datos del comprador al servidor
     * @param credenciales los datos del comprador
     * @returns 
     */

    registrarC(credenciales: {correoC:string,nombreC:string,telefonoC : string,
    estadoC : string,
    ciudadC : string,
    coloniaC : string,
    cpC : string,
    calleC : string,
    numeroC : number}): Observable<IRegistrar>{
        return this._http.post<IRegistrar>(this._url+"/createC",credenciales);
    }

    /**
     * Metodo para mandar los datos 
     * @param credenciales 
     * @returns 
     */
    registrarV(credenciales: {correoV:string,nombreV:string,telefonoV : string,
        estadoV : string,
        ciudadV : string,
        coloniaV : string,
        cpV : string,
        calleV : string,
        numeroV : number,
        tarjetaV : String
    }): Observable<IRegistrar>{
            return this._http.post<IRegistrar>(this._url+"/createV",credenciales);
        }

    
}
