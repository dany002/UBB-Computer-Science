import React, {useEffect, useState} from 'react';
import {View, Text, StyleSheet, ActivityIndicator, Button} from 'react-native';
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';
import Toast from 'react-native-toast-message';
import NetInfo from '@react-native-community/netinfo';
import WebSocketClient from "../websocket/WebSocketClient";
import {useNavigation} from "@react-navigation/native";
import {appendLog} from "../log/Logger";

const CarDetailsScreen = ({route}) => {
    const navigation = useNavigation();
    const carId = route.params.id;
    const [carDetails, setCarDetails] = useState(null);
    const [isOffline, setIsOffline] = useState(false);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        const unsubscribe = NetInfo.addEventListener(state => {
            setIsOffline(!state.isConnected);
            if (state.isConnected) {
                loadCarDetails();
            }

        });

        loadCarDetails();

        return () => unsubscribe();
    }, [carId]);

    const handleWebSocketMessage = (data) => {
        try {
            const car = JSON.parse(data);
            Toast.show({
                type: 'info',
                text1: 'New Car Added',
                text2: `Car: ${car.name}`,
                visibilityTime: 5000,
                onPress: () => {
                    navigation.navigate('CarDetails', {id: car.id})
                },
            });
            appendLog('New car added');
        } catch (error) {
            appendLog('Error parsing WebSocket message');
        }
    };

    WebSocketClient(handleWebSocketMessage);

    const loadCarDetails = async () => {
        setIsLoading(true);
        const storedCarDetails = await getData(`@carDetails_${carId}`);

        if (isOffline) {
            if (storedCarDetails) {
                setCarDetails(storedCarDetails);
            } else {
                setIsOffline(true);
            }
            setIsLoading(false);
            return;
        }

        try {
            const response = await axios.get(`http://192.168.1.134:2406/car/${carId}`);
            const event = response.data;
            setCarDetails(event);
            await storeData(`@carDetails_${carId}`, event);
            setIsOffline(false);
            appendLog('Event details fetched successfully from server');
        } catch (error) {
            if (storedCarDetails) {
                setCarDetails(storedCarDetails);
                appendLog('Loaded car details from AsyncStorage');
            } else {
                Toast.show({
                    type: 'error',
                    text1: 'Error',
                    text2: 'Failed to fetch event details.',
                    visibilityTime: 5000,
                });
                setIsOffline(true);
                appendLog('Error fetching event details');
            }
        } finally {
            setIsLoading(false);
        }
    };

    const storeData = async (key, value) => {
        try {
            const jsonValue = JSON.stringify(value);
            await AsyncStorage.setItem(key, jsonValue);
            appendLog('Storing data in AsyncStorage');
        } catch (e) {
            appendLog('Error storing data');
        }
    };

    const getData = async (key) => {
        try {
            const jsonValue = await AsyncStorage.getItem(key);
            appendLog('Retrieving data from AsyncStorage');
            return jsonValue != null ? JSON.parse(jsonValue) : null;
        } catch (e) {
            appendLog('Error retrieving data');
        }
    };

    return (
        <View style={styles.container}>
            {isLoading ? (
                <ActivityIndicator size="large" color="#0000ff"/>
            ) : isOffline && !carDetails ? (
                <View style={styles.offlineContainer}>
                    <Text style={styles.offlineText}>You are offline</Text>
                    <Button title="Retry" onPress={loadCarDetails} color="#007AFF"/>
                </View>
            ) : carDetails ? (
                <View>
                    <Text style={styles.eventTitle}>{carDetails.name}</Text>
                    <Text style={styles.eventInfo}>{`ID: ${carDetails.id}`}</Text>
                    <Text style={styles.eventInfo}>{`Supplier: ${carDetails.supplier}`}</Text>
                    <Text style={styles.eventInfo}>{`Details: ${carDetails.details}`}</Text>
                    <Text style={styles.eventInfo}>{`Status: ${carDetails.status}`}</Text>
                    <Text style={styles.eventInfo}>{`Quantity: ${carDetails.quantity}`}</Text>
                    <Text style={styles.eventInfo}>{`Type: ${carDetails.type}`}</Text>
                </View>
            ) : null}
            <Toast/>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        padding: 16,
    },
    offlineContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        paddingHorizontal: 20,
    },
    offlineText: {
        fontSize: 18,
        color: '#333',
        marginBottom: 10,
    },
    carTitle: {
        fontSize: 24,
        fontWeight: 'bold',
        marginBottom: 10,
    },
    carInfo: {
        fontSize: 18,
        marginBottom: 8,
    },
});

export default CarDetailsScreen;