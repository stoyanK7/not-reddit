export default function PostActions() {
    return (
        <div className="flex gap-2 text-reddit-gray hover:cursor-pointer">
            <div className="flex items-center">
                <span className="p-2 mr-1 rounded-sm hover:bg-reddit-gray-hover hover:text-reddit-orange">
                    Up
                </span>
                <span className="font-bold text-reddit-black">134</span>
                <span className="p-2 ml-1 rounded-sm hover:bg-reddit-gray-hover hover:text-reddit-blue">
                    Down
                </span>
            </div>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Comments
            </div>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Award
            </div>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Share
            </div>
            <div className="p-2 rounded-sm hover:bg-reddit-gray-hover">
                Save
            </div>
        </div>
    )
}