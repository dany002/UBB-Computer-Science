import React, {useEffect, useState} from 'react';
import {View, Text, FlatList, StyleSheet, ActivityIndicator, TouchableOpacity} from 'react-native';
import axios from 'axios';
import {useNavigation} from "@react-navigation/native";
import Toast from "react-native-toast-message";
import {appendLog} from "../log/Logger";


const StaffScreen = () => {
    const navigation = useNavigation();
    const [carTypes, setCarTypes] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    useEffect(() => {
        loadCarTypes();
    }, []);

    const loadCarTypes = async () => {
        setIsLoading(true);
        try {
            const response = await axios.get('http://192.168.1.134:2406/carstypes');
            const groupedCars = response.data.reduce((acc, car) => {
                // Check if the car type already exists in the accumulator object
                if (acc[car.type]) {
                    // If it exists, add the quantity to the existing sum
                    acc[car.type] += car.quantity;
                } else {
                    // If it doesn't exist, initialize the sum with the quantity
                    acc[car.type] = car.quantity;
                }
                return acc;
            }, {});

            // Convert the groupedCars object into an array of objects
            const carTypesArray = Object.keys(groupedCars).map(type => ({
                type,
                quantity: groupedCars[type]
            }));


            setCarTypes(carTypesArray);
            appendLog('Fetched car types successfully');
        } catch (error) {
            appendLog('Error fetching in progress events');
        } finally {
            setIsLoading(false);
        }
    };

    const requestType = async (carType) => {
        try {
            await axios.put(`http://192.168.1.134:2406/requestcar/${carType}`);
            Toast.show({
                type: 'success',
                text1: 'Type requested',
                text2: `Type: ${carType}`,
                visibilityTime: 5000,
            });

            appendLog('Type car requested successfully');
            loadCarTypes();
        } catch (error) {
            appendLog('Error request type car');
        }
    };

    return (
        <View style={styles.container}>
            {isLoading ? (
                <ActivityIndicator size="large" color="#0000ff"/>
            ) : (
                <FlatList
                    data={carTypes}
                    keyExtractor={(item) => item.type.toString()}
                    showsVerticalScrollIndicator={false}
                    renderItem={({item}) => (
                        <View style={styles.eventItem}>
                            <Text style={styles.title}>{item.type}</Text>
                            <Text>Quantity: {item.quantity}</Text>
                            <TouchableOpacity
                                style={styles.enrollButton}
                                onPress={() => {
                                    requestType(item.type);
                                }}
                            >
                                <Text style={styles.enrollButtonText}>Request</Text>
                            </TouchableOpacity>
                        </View>
                    )}
                />
            )}
            <Toast/>
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#f2f2f2',
        padding: 10,
    },
    eventItem: {
        backgroundColor: '#fff',
        padding: 10,
        marginVertical: 8,
        borderRadius: 5,
    },
    title: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    enrollButton: {
        backgroundColor: '#007AFF',
        padding: 10,
        borderRadius: 5,
        marginTop: 10,
    },
    enrollButtonText: {
        color: '#fff',
        fontSize: 16,
        fontWeight: 'bold',
        textAlign: 'center',
    }
});

export default StaffScreen;