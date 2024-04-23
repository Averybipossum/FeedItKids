import { Stack } from "expo-router";

export default function Layout() {
    return (
        <Stack screenOptions={{
            headerStyle: {
                backgroundColor: "orange"
            },
            headerTintColor: "white",
            headerTitleStyle: {
                fontWeight: "bold"
            },
            headerTitleAlign: "center"

        }} />

    )
}