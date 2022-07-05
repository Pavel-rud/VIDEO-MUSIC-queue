import { createRouter, createWebHashHistory } from 'vue-router'

import Home from '../components/HomePage'
import LoginUser from '../components/LoginUser'
import RegisterUser from '../components/RegisterUser'
import LogoutUser from '../components/LogoutUser'
import ProfilePage from "../components/ProfilePage";
import CreateRoom from "../components/CreateRoom";

const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/' },
        { path: '/login', component: LoginUser },
        { path: '/home', component: Home },
        { path: '/register', component: RegisterUser },
        { path: '/logout', component: LogoutUser },
        {path: '/profile', component: ProfilePage},
        {path: '/createroom', component: CreateRoom},
    ]
})

export default router