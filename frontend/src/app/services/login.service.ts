import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';

/**
 * Interface para declarar los datos que vamos a ocupar en el subscribe
 */
export interface ILogin {

    session:string; // el correo que es la sesion que nos regresa el servidor
    msg:string;  // el mensaje que nos regresa cuando se haga la petición
    nombre:string; // el nombre del que inica sesion

    //Los datos del comprador
    
    correoC: String;
    contraseniaC: String;

    //Los datos del vendedor

    correoV: String; 
    contraseniaV: String;

}

@Injectable({
    providedIn: 'root'
  })

/**
 * La clase del servicio de login para que subscriba el componente login
 */
export class LoginService{
    
    private _url = 'http://127.0.0.1:5000'; //la url del servidor para mandar las peticiones
    /**
     * Constructor de la clase
     * @param _http el clliente para generar las petciones por json 
     */

    constructor(private _http: HttpClient){}

    /**
     * Metodo para madnar los datos del comprador
     * @param credenciales los datos del comprador para poder inciar sesión
     * @returns un JSON con un mensaje de error si los datos son incorrectos y un mensaje de éxito
     * si los datos son correctos y dejarlo inicar sesión
     */
  
    IniciarSesionC(credenciales: {correoC:string, contraseniaC:string}): Observable<ILogin>{
        return this._http.post<ILogin>(this._url+"/loginC",credenciales);
    }   

    /**
     * Metodo para mandar los datos del vendedor
     * @param credenciales los datos del vendedor para poder inciar sesión
     * @returns  un JSON con un mensaje de error si los datos son incorrectos y un mensaje de éxito
     * si los datos son correctos y dejarlo inicar sesión
     */

    IniciarSesionV(credenciales: {correoV:string, contraseniaV:string}): Observable<ILogin>{
        return this._http.post<ILogin>(this._url+"/loginV",credenciales);
    }
}

