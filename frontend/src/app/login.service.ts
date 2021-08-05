import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';
import {HttpParams} from "@angular/common/http";

export interface ILogin {


    correoC: String;
    contraseniaC: String;

    correoV: String;
    contraseniaV: String;
    

}

@Injectable({
    providedIn: 'root'
  })
export class LoginService{
    private _url = 'http://127.0.0.1:5000';
    constructor(private _http: HttpClient){}

    IniciarSesionC(credenciales: {correoC:string, contraseniaC:string}): Observable<ILogin>{
       console.log(credenciales)
        return this._http.post<ILogin>(this._url+"/loginC",credenciales);
    }

    IniciarSesionV(credenciales: {correoV:string, contraseniaV:string}): Observable<ILogin>{
        //console.log(credenciales)
         return this._http.post<ILogin>(this._url+"/loginV",credenciales);
     }
 



    
}

