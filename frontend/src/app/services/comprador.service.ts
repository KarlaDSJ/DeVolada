import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

export interface IComprador {  
  correo: string,
  nombre: string, 
  telefono: string,
  contrasenia: string
  
}

@Injectable({
  providedIn: 'root'
})
export class CompradorService {

  private _url = "http://127.0.0.1:5000";

  constructor(private _http: HttpClient) { }

  /**
   * Obtiene la información de un comprador.
   * @param correo correo del comprador
   * @returns Información del comprador con formato IComprador
   */
  async obtenerDatos(correo: string): Promise<IComprador> {
    return this._http.get<IComprador>(this._url + "/comprador/"+correo, {}).toPromise()
  }
}
