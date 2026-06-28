// swift-tools-version: 6.0
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "EmpireOS",
    platforms: [.macOS(.v14)],
    products: [
        .executable(name: "EmpireOS", targets: ["EmpireOS"]),
        .library(name: "EmpireOSKit", targets: ["EmpireOSKit"]),
        .executable(name: "empire-cli", targets: ["empire-cli"]),
    ],
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser.git", from: "1.3.0"),
        .package(url: "https://github.com/apple/swift-markdown.git", from: "0.3.0"),
        .package(url: "https://github.com/apple/swift-syntax.git", from: "600.0.0"),
        .package(url: "https://github.com/apple/swift-async-algorithms.git", from: "1.0.0"),
        .package(url: "https://github.com/apple/swift-crypto.git", from: "3.0.0"),
        .package(url: "https://github.com/apple/swift-collections.git", from: "1.1.0"),
        .package(url: "https://github.com/apple/swift-log.git", from: "1.6.0"),
        .package(url: "https://github.com/daltoniam/Starscream.git", from: "4.0.8"),
        .package(url: "https://github.com/Alamofire/Alamofire.git", from: "5.9.0"),
        .package(url: "https://github.com/groue/GRDB.swift.git", from: "6.27.0"),
        .package(url: "https://github.com/SnapKit/SnapKit.git", from: "5.7.0"),
        .package(url: "https://github.com/pointfreeco/swift-snapshot-testing.git", from: "1.17.0"),
    ],
    targets: [
        .executableTarget(
            name: "EmpireOS",
            dependencies: [
                "EmpireOSKit",
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
            ],
            path: "app-shell"
        ),
        .target(
            name: "EmpireOSKit",
            dependencies: [
                .product(name: "Markdown", package: "swift-markdown"),
                .product(name: "SwiftSyntax", package: "swift-syntax"),
                .product(name: "SwiftParser", package: "swift-syntax"),
                .product(name: "AsyncAlgorithms", package: "swift-async-algorithms"),
                .product(name: "Crypto", package: "swift-crypto"),
                .product(name: "Collections", package: "swift-collections"),
                .product(name: "Logging", package: "swift-log"),
                .product(name: "Starscream", package: "Starscream"),
                .product(name: "Alamofire", package: "Alamofire"),
                .product(name: "GRDB", package: "GRDB.swift"),
                .product(name: "SnapKit", package: "SnapKit"),
            ],
            path: ".",
            exclude: ["app-shell", "empire-cli", "Tests"],
            sources: [
                "dashboard",
                "chat-zone",
                "agent-room",
                "coding-zone",
                "co-work-zone",
            ]
        ),
        .executableTarget(
            name: "empire-cli",
            dependencies: [
                "EmpireOSKit",
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
            ],
            path: "empire-cli"
        ),
        .testTarget(
            name: "EmpireOSTests",
            dependencies: ["EmpireOS", "EmpireOSKit"],
            path: "Tests"
        ),
    ]
)
