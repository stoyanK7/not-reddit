import { AuthenticatedTemplate, UnauthenticatedTemplate } from "@azure/msal-react";
import Image from "next/image";
import Link from "next/link";

import getUsername from "@/utils/getUsername";

import LogoutButton from "./LogoutButton";

export default function Navbar() {
    return (
        <nav
            className="w-full h-20 bg-white p-2 top-0 fixed grid grid-cols-[1fr_auto] grid-rows-1
            shadow-reddit z-10">
            <Link
                href="/">
                <div
                    className="relative overflow-visible h-full">
                    <Image
                        style={{ objectFit: "contain" }}
                        src="/logo-full.png"
                        alt="Application logo"
                        fill
                        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                    />
                </div>
            </Link>
            <div
                className="ml-auto">
                <UnauthenticatedTemplate>
                    <Link
                        href="/auth">
                        <button
                            className="h-full rounded-sm bg-reddit-orange text-white px-8">
                            Login
                        </button>
                    </Link>
                </UnauthenticatedTemplate>
                <AuthenticatedTemplate>
                    <span
                        className="mr-2 font-bold">
                        {typeof window !== "undefined" && getUsername()}
                    </span>
                    <LogoutButton />
                </AuthenticatedTemplate>
            </div>
        </nav>
    );
}
