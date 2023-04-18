import Link from "next/link";
import Image from "next/image";

export default function CreatePost() {
    return (
        <div className="flex w-full items-center gap-2 text-reddit-gray bg-white rounded-sm
        shadow-reddit border border-reddit-postline mb-4 p-2">
            <Link href="/r/all" passHref legacyBehavior>
                <a className="relative w-10 h-10 grow-0">
                    <Image
                        style={{ objectFit: 'contain' }}
                        alt="User avatar"
                        src="/redditor.png"
                        fill />
                </a>
            </Link>
            <Link className="flex-grow" href="/post/create">
                <input className="rounded-sm px-4 py-2 border-2 border-transparent bg-[#F6F7F8]
                hover:border-blue w-full"
                type="text"
                placeholder="Create Post" />
            </Link>
            <Link href="/post/create?image" className="p-2 rounded-sm text-2xl
                hover:bg-reddit-gray-hover grow-0">
                <span>Image</span>
            </Link>
            <Link href="/post/create?link" className="p-2 rounded-sm text-2xl
                hover:bg-reddit-gray-hover grow-0">
                <span>Link</span>
            </Link>
        </div>
    )
}
