import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";


@Injectable()
export class LoginService{
    private _LoginUrl = 'http://127.0.0.1:5000/';
    constructor(private _http: HttpClient){}

    getProducts(){
        return this._http.get(this._LoginUrl)
    }

}

