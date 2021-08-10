import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from 'rxjs';
import {HttpParams} from "@angular/common/http";

export interface IRegistrar {

    msg:string;
    correoC:string,
    nombreC:string,
    telefonoC : number,
    estadoC : string,
    ciudadC : string,
    coloniaC : string,
    cpC : string,
    calleC : string,
    numeroC : number

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
export class RegistrarService{
    private _url = 'http://127.0.0.1:5000/';
    constructor(private _http: HttpClient){}

    registrarC(credenciales: {correoC:string,nombreC:string,telefonoC : string,
    estadoC : string,
    ciudadC : string,
    coloniaC : string,
    cpC : string,
    calleC : string,
    numeroC : number}): Observable<IRegistrar>{
        return this._http.post<IRegistrar>(this._url+"/createC",credenciales);
    }
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
