export default function SortBy({ sortBy, setSortBy }) {
    return (
        <div
            className="flex gap-2 w-full bg-white p-2">
            <div
                onClick={() => setSortBy("latest")}
                className={`p-2 text-green-600 rounded-sm hover:bg-green-300
                hover:cursor-pointer ${sortBy === "latest" ? "bg-green-300" : ""}`}>
                Latest
            </div>
            <div
                onClick={() => setSortBy("hot")}
                className={`p-2 text-orange-600 rounded-sm hover:bg-orange-300
                hover:cursor-pointer ${sortBy === "hot" ? "bg-orange-300" : ""}`}>
                Hot
            </div>
        </div>
    );
}

