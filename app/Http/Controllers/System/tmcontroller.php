<?php

namespace App\Http\Controllers\System;

use Illuminate\Http\Request;
use App\Http\Controllers\Controller;

class tmcontroller extends Controller
{
    //
    public function tmcontroller(){
        return view('system/recommender/tmview');
    }
    
}
